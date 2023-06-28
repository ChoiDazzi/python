package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity6 extends AppCompatActivity {
    EditText et;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main6);

        et = findViewById(R.id.et);
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
        String e = et.getText().toString();
        int ee = Integer.parseInt(e);
        String txt = "";

        for(int i = 1; i<10; i++) {
            txt += ee + "*" + i + "=" + ee*i + "\n";
        }


        tv.setText(txt);
    }
}