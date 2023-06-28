package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity3 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        TextView et1 = findViewById(R.id.et1);
        TextView et2 = findViewById(R.id.et2);
        TextView et3 = findViewById(R.id.et3);

        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            int num1 = Integer.parseInt(et1.getText().toString());
            int num2 = Integer.parseInt(et2.getText().toString());
            int total = 0;
            @Override
            public void onClick(View view) {
                for(int i=num1; i<=num2; i++){
                    total += i;
                }
                et3.setText(total+"");
            }
        });
    }
}