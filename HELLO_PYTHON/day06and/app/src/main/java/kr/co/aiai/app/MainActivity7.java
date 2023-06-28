package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity7 extends AppCompatActivity {
    EditText et1;
    EditText et2;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main7);
        et1 = findViewById(R.id.et_first);
        et2 = findViewById(R.id.et_last);

        tv = findViewById(R.id.tv);
        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }

    public void myclick() {
        int start = Integer.parseInt(et1.getText().toString());
        int end = Integer.parseInt(et2.getText().toString());
        String txt = "";
        for (int i = start; i <= end; i++) {
            for (int j = 1; j <= i; j++) {
                txt += "*";
            }
            txt += "\n";
        }

        tv.setText(txt);
    }
}