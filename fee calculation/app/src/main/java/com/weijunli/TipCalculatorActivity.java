package com.weijunli;

import android.annotation.SuppressLint;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.RadioGroup;
import android.widget.Switch;
import android.widget.EditText;
import android.widget.Button;
import android.widget.TextView;
import android.widget.RadioButton;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import java.text.NumberFormat;

public class TipCalculatorActivity extends AppCompatActivity {

    private EditText costOfServiceEditText;
    private RadioGroup tipOptionsRadioGroup;
    private Switch roundUpSwitch;
    private Button calculateButton;
    private TextView tipResultTextView;
    private TextView tipAmount;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        costOfServiceEditText = findViewById(R.id.cost_of_service);
        tipOptionsRadioGroup = findViewById(R.id.tip_options);
        roundUpSwitch = findViewById(R.id.round_up_switch);
        calculateButton = findViewById(R.id.calculate_button);
        tipResultTextView = findViewById(R.id.tip_result);
        tipAmount = findViewById(R.id.tip_amount);

        calculateButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    calculateTip();
                } catch (Exception e) {
                    AlertDialog.Builder builder = new AlertDialog.Builder(TipCalculatorActivity.this);
                    builder.setTitle("错误");
                    builder.setMessage("请输入正确的数字");
                    builder.setPositiveButton("确定", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            // 点击确定按钮后的操作
                            dialog.dismiss();  // 关闭弹窗
                        }
                    });
                    builder.show();
                }
            }
        });
    }

    private void calculateTip() {
        String stringInTextField = costOfServiceEditText.getText().toString();
        double cost = Double.parseDouble(stringInTextField);

        double tipPercentage = 0.0;
        int checkedRadioButtonId = tipOptionsRadioGroup.getCheckedRadioButtonId();
        if (checkedRadioButtonId == R.id.option_twenty_percent) {
            tipPercentage = 0.20;
        } else if (checkedRadioButtonId == R.id.option_eighteen_percent) {
            tipPercentage = 0.18;
        } else if (checkedRadioButtonId == R.id.option_ten_percent) {
            tipPercentage = 0.10;
        } else {
            tipPercentage = 0.15;
        }

        double tip = tipPercentage * cost;
        if (roundUpSwitch.isChecked()) {
            tip = Math.ceil(tip);
        }

        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();
        String formattedTip1 = currencyFormat.format(tip);
        double total = tip + cost;
        total = Math.floor(total);
        String formattedTip2 = currencyFormat.format(total);

        tipAmount.setText(getString(R.string.tip_amount) + " " + formattedTip1);
        tipResultTextView.setText(getString(R.string.tip_result) + " " + formattedTip2);
    }
}
