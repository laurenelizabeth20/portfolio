package com.example.mathapp;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import java.util.Random;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Random rand = new Random();
    int upperbound = 100;
    //generate random values from 0-100
    int value1 = rand.nextInt(upperbound);;
    int value2 = rand.nextInt(upperbound);;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView Number1 = findViewById(R.id.Number1);
        Number1.setText(""+value1);
        TextView Number2 = findViewById(R.id.Number2);
        Number2.setText(""+value2);

    }
    public void onSubmitClick (View view){
        TextView Answer = findViewById(R.id.Answer);
        EditText Attempt = findViewById(R.id.Attempt);
        int userAnswer = Integer.parseInt(Attempt.getText().toString());
        if(userAnswer == value1+value2) {
            Answer.setText("Correct!");

        } else {
            Answer.setText("Wrong, the correct answer was: " + (value1+value2));
        }

    }
}