import torch
import os
from tqdm import tqdm
import pandas as pd
import numpy as np
from model import SpamClf
from transformers import BertModel, BertTokenizer
from sklearn.metrics import classification_report

from utils import *
from preprocessing import preprocessing_data


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# load trained model
save_dir = f"models/"
model_name = "bert-base-uncased"
bert_tokenizer = BertTokenizer.from_pretrained(model_name)
bert_model = BertModel.from_pretrained(model_name)
spam_clf = SpamClf(bert_model).to(device)
# spam_clf.load_state_dict(torch.load(f"{save_dir}/pytorch_model.bin"))
spam_clf.load_state_dict(torch.load(f"{save_dir}/pytorch_model.pt"))

spam_clf.eval()

# ask user for msg
# input_msg = input(f"please send the message: \n")

input_msg = r"""
FREE for 1st week! No1 Nokia tone 4 ur mobile every week just txt NOKIA to 8077 Get txting and tell ur mates. www.getzed.co.uk POBox 36504 W45WQ 16+ norm150p/tone
"""
print(f"input_msg: {input_msg}")

# tokenization
msg_tokens = tokenize_function([input_msg], model_name).to(device)

# input msg to model
preds = spam_clf(msg_tokens)
preds = torch.argmax(preds, dim=1)
output = "ham" if preds == 0 else "spam"
print(f"output: {output}")

# finde the url in spam
if output == "spam":
    print("Urls: ", find_spam_url(input_msg))


print(
    f" ----------------------- testing the spam dectetor model ----------------------- "
)
# testing on testing set
preprocessed_out = preprocessing_data("spam/raw_spam.csv", model_name)
test_dataloader = preprocessed_out["test_dataloader"]
test_df = preprocessed_out["test_df"]
# save test set for future testing
test_set = pd.DataFrame()
test_set["Message"] = np.array(test_df["Message"])
test_set["Category"] = np.array(test_df["Category"])
test_set.to_csv(f"ML/spam/test_set.csv", index=False)

print(f"ham amount: {len(test_df[test_df['Category'] == 'ham'])}")
print(f"spam amount: {len(test_df[test_df['Category'] == 'spam'])}")

# extract spam from test_set for future testing
spam_test = test_df[test_df["Category"] == "spam"]
spam_set = pd.DataFrame()
spam_set["Message"] = np.array(spam_test["Message"])
spam_set["Category"] = np.array(spam_test["Category"])
spam_set.to_csv(f"ML/spam/spam_set.csv", index=False)

# input test set to model
prediction_data = predict(spam_clf, test_dataloader, device)
y_true = test_df.target.values

# show testing performance
perform_test = classification_report(y_true, prediction_data["predictions"])
print("-" * 60)
print(f"perform_test: ")
print(perform_test)
print("-" * 60)


r"""
https://www.baidu.com/s?wd=%E4%B8%93%E5%AE%B6%E5%BB%BA%E8%AE%AE%E5%BC%80%E6%94%BE%E5%9B%BD%E9%99%85%E5%A9%9A%E5%A7%BB+%E8%A7%A3%E5%86%B3%E5%89%A9%E7%94%B7%E9%97%AE%E9%A2%98&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1 

Spam: 
1. "Hi. Customer Loyalty Offer :The NEW Nokia6650 Mobile from ONLY £10 at TXTAUCTION! Txt word: START to No: 81151 & get yours Now! 4T&Ctxt TC 150p/MTmsg"
2. "U are subscribed to the best Mobile Content Service, , in the UK for £3 per 10 days until you send STOP to 82324. Helpline 08706091795"
3. Urgent Ur £500 guaranteed award is still unclaimed! Call 09066368327 NOW closingdate04/09/02 claimcode M39M51 £1.50pmmorefrommobile2Bremoved-MobyPOBox734LS27YF
4. UR awarded a City Break and could WIN a £200 Summer Shopping spree every WK. Txt STORE to 88039 . SkilGme. TsCs087147403231Winawk!Age16 £1.50perWKsub
5. FREE for 1st week! No1 Nokia tone 4 ur mobile every week just txt NOKIA to 8077 Get txting and tell ur mates. www.getzed.co.uk POBox 36504 W45WQ 16+ norm150p/tone
6. Last Chance! Claim ur £150 worth of discount vouchers today! Text SHOP to 85023 now! SavaMob, offers mobile! T Cs SavaMob POBOX84, M263UZ. £3.00 Sub. 16
7. You have won a guaranteed £200 award or even £1000 cashto claim UR award call free on 08000407165 (18+) 2 stop getstop on 88222 PHP. RG21 4JX
8. Congratulations ur awarded either £500 of CD gift vouchers & Free entry 2 our £100 weekly draw txt MUSIC to 87066 TnCs www.Ldew.com1win150ppmx3age16

Ham: 
1. Sun cant come to earth but send luv as rays. cloud cant come to river but send luv as rain. I cant come to meet U, but can send my care as msg to U. Gud evng
2. Maybe?! Say hi to  and find out if  got his card. Great escape or wetherspoons?
3. It just seems like weird timing that the night that all you and g want is for me to come smoke is the same day as when a shitstorm is attributed to me always coming over and making everyone smoke
4. Height of Confidence: All the Aeronautics professors wer calld &amp; they wer askd 2 sit in an aeroplane. Aftr they sat they wer told dat the plane ws made by their students. Dey all hurried out of d plane.. Bt only 1 didnt move... He said:""if it is made by my students,this wont even start........ Datz confidence..
5. Macha dont feel upset.i can assume your mindset.believe me one evening with me and i have some wonderful plans for both of us.LET LIFE BEGIN AGAIN.call me anytime
6. The world is running and i am still.maybe all are feeling the same,so be it.or i have to admit,i am mad.then where is the correction?or let me call this is life.and keep running with the world,may be u r also running.lets run.
7. Just got up. have to be out of the room very soon. …. i hadn't put the clocks back til at 8 i shouted at everyone to get up and then realised it was 7. wahay. another hour in bed.

"""
