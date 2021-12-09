package com.example.audiorecord;

import android.Manifest;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.graphics.drawable.Drawable;
import android.media.AudioFormat;
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
import com.example.audiorecord.databinding.ActivityMainBinding;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;
    private static MediaRecorder mediaRecorder;
    private static MediaPlayer mediaPlayer;
    private static String audioFilePath;
    private boolean isRecording = false;
    private static final int RECORD_REQUEST_CODE = 101;
    private static final int STORAGE_REQUEST_CODE = 102;
    public int[] cardlist = new int[5];
    long recordStart; //종모양
    long now; //덱 누를떄


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        View view = binding.getRoot();
        setContentView(view);
        audioSetup();
        cardlist[0] = R.drawable.card1;
        cardlist[1] = R.drawable.card2;
        cardlist[2] = R.drawable.card4;
        cardlist[3] = R.drawable.card5;
        cardlist[4] = R.drawable.card6;
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("Game Start");
        builder.setMessage("게임을 시작하시겠습니까?");
        builder.setPositiveButton("네",
                new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        recordAudio(view);
                    }
                });
        builder.show();
    }

    protected boolean hasMicrophone(){
        PackageManager packageManager = this.getPackageManager();
        return packageManager.hasSystemFeature(PackageManager.FEATURE_MICROPHONE);
    }

    private void audioSetup(){
        if(!hasMicrophone()){

            binding.stopRecord.setEnabled(false);
        }else{

        }

        audioFilePath = this.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS).getAbsolutePath()+"/myaudio.aac"; // file extension과 관련 없이 aac로 인코딩 함.

        requestPermission(Manifest.permission.RECORD_AUDIO, RECORD_REQUEST_CODE);
    }

    public void recordAudio(View view){
        isRecording = true;
        binding.stopRecord.setEnabled(true);


        try{
            mediaRecorder = new MediaRecorder();
            mediaRecorder.setAudioSource(MediaRecorder.AudioSource.CAMCORDER);
            mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.AAC_ADTS);
            mediaRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AAC);
            mediaRecorder.setAudioEncodingBitRate(128000);
            mediaRecorder.setAudioSamplingRate(96000);
            mediaRecorder.setAudioChannels(2);
            mediaRecorder.setOutputFile(audioFilePath);
            mediaRecorder.prepare();
        }catch(Exception e){
            e.printStackTrace();
        }

        mediaRecorder.start();
    }

    public void stopAudio(View view){ //종 버튼 클릭하면 실행되는 함수
        binding.stopRecord.setEnabled(false);
        int now;


        if(isRecording){
            mediaRecorder.stop();
            mediaRecorder.release();
            mediaRecorder = null;
            isRecording = false;
        }else{
            mediaPlayer.release();
            mediaPlayer = null;
        }
        Log.e("path", this.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS).getAbsolutePath());
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
            Python python = Python.getInstance();
            PyObject pyObj = python.getModule("Split2Stereo&Filtering");
            PyObject librosa = python.getModule("librosa");

            long left = pyObj.get("left").toLong();
            long right = pyObj.get("right").toLong();
            if(left < right){
                AlertDialog.Builder builder2 = new AlertDialog.Builder(this);
                builder2.setTitle("Game Finished");
                builder2.setMessage("Player 1 wins");
                builder2.setPositiveButton("다시 시작",
                        new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                recordAudio(view);
                            }
                        });
                builder2.show();
            }
            else if(right < left){
                AlertDialog.Builder builder2 = new AlertDialog.Builder(this);
                builder2.setTitle("Game Finished");
                builder2.setMessage("Player 2 wins");
                builder2.setPositiveButton("다시 시작",
                        new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                recordAudio(view);
                            }
                        });
                builder2.show();
            }
            else{

            }



        }



    }

    public void playAudio(View view) throws IOException {
        binding.stopRecord.setEnabled(false);


        mediaPlayer = new MediaPlayer();
        mediaPlayer.setDataSource(audioFilePath);
        mediaPlayer.prepare();
        mediaPlayer.start();
    }

    public void ondeck1Click(View view){
        TextView turn = findViewById(R.id.Turn);
        turn.setText("Player 2 Turn");
        TextView open1 = findViewById(R.id.openCardNum1);
        TextView deck1 = findViewById(R.id.deckNum1);
        int num1 = Integer.parseInt(open1.getText().toString());
        int deck = Integer.parseInt(deck1.getText().toString());
        deck1.setText("" + (deck - 1));
        open1.setText("" + (num1 + 1));
        ImageView img = findViewById(R.id.openCard1);
        Random random = new Random();
        Drawable drawable = getResources().getDrawable(cardlist[random.nextInt(5)]);
        img.setImageDrawable(drawable);
    }

    public void ondeck2Click(View view){
        TextView turn = findViewById(R.id.Turn);
        turn.setText("Player 1 Turn");
        TextView open2 = findViewById(R.id.openCardNum2);
        TextView deck2 = findViewById(R.id.deckNum2);
        int num2 = Integer.parseInt(open2.getText().toString());
        int deck = Integer.parseInt(deck2.getText().toString());
        deck2.setText("" + (deck - 1));
        open2.setText("" + (num2 + 1));
        ImageView img = findViewById(R.id.openCard2);
        Random random = new Random();
        Drawable drawable = getResources().getDrawable(cardlist[random.nextInt(5)]);
        img.setImageDrawable(drawable);
    }

    public void onPlayer1WinClick(View view){
        TextView open1 = findViewById(R.id.openCardNum1);
        TextView open2 = findViewById(R.id.openCardNum2);
        TextView deck1 = findViewById(R.id.deckNum1);
        int num1 = Integer.parseInt(open1.getText().toString());
        int num2 = Integer.parseInt(open2.getText().toString());
        int deck = Integer.parseInt(deck1.getText().toString());
        deck1.setText("" + (num1 + num2 + deck));
        open1.setText("0");
        open2.setText("0");

        
        Drawable drawable = getResources().getDrawable(R.drawable.card3);
        ImageView o1 = findViewById(R.id.openCard1);
        ImageView o2 = findViewById(R.id.openCard2);
        o1.setImageDrawable(drawable);
        o2.setImageDrawable(drawable);
    }
    public void onPlayer2WinClick(View view){
        TextView open1 = findViewById(R.id.openCardNum1);
        TextView open2 = findViewById(R.id.openCardNum2);
        TextView deck2 = findViewById(R.id.deckNum2);
        int num1 = Integer.parseInt(open1.getText().toString());
        int num2 = Integer.parseInt(open2.getText().toString());
        int deck = Integer.parseInt(deck2.getText().toString());
        deck2.setText("" + (num1 + num2 + deck));
        open1.setText("0");
        open2.setText("0");

        Drawable drawable = getResources().getDrawable(R.drawable.card3);
        ImageView o1 = findViewById(R.id.openCard1);
        ImageView o2 = findViewById(R.id.openCard2);
        o1.setImageDrawable(drawable);
        o2.setImageDrawable(drawable);
    }

    public void onPenalty1Click(View view){
        // decknum1 - 1
        // decknum2 + 1
        TextView deck1 = findViewById(R.id.deckNum1);
        TextView deck2 = findViewById(R.id.deckNum2);

        int num1 = Integer.parseInt(deck1.getText().toString());
        int num2 = Integer.parseInt(deck2.getText().toString());

        deck1.setText(""+(num1-1));
        deck2.setText(""+(num2+1));

    }
    public void onPenalty2Click(View view){
        // decknum2 - 1
        // decknum1 + 1
        TextView deck1 = findViewById(R.id.deckNum1);
        TextView deck2 = findViewById(R.id.deckNum2);

        int num1 = Integer.parseInt(deck1.getText().toString());
        int num2 = Integer.parseInt(deck2.getText().toString());

        deck1.setText(""+(num1+1));
        deck2.setText(""+(num2-1));
    }

    protected void requestPermission(String permissionType, int requestCode){
        int permission = ContextCompat.checkSelfPermission(this, permissionType);
        if(permission != PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(this, new String[]{permissionType}, requestCode);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults){
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        switch(requestCode){
            case RECORD_REQUEST_CODE:{
                if(grantResults.length==0 || grantResults[0]!=PackageManager.PERMISSION_GRANTED){

                    Toast.makeText(this, "RECORD PERMISSION REQUIRED", Toast.LENGTH_LONG).show();
                }else{
                    requestPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE, STORAGE_REQUEST_CODE);
                }
            }
            case STORAGE_REQUEST_CODE:{
                if(grantResults.length==0 || grantResults[0]!=PackageManager.PERMISSION_GRANTED){
                    Toast.makeText(this, "EXTERNAL STORAGE PERMISSION REQUIRED", Toast.LENGTH_LONG).show();
                }
            }
        }
    }


}