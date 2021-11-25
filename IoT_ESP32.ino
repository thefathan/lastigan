#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <MySQL_Encrypt_Sha1.h>
#include <MySQL_Packet.h>

#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>

// WIFI CREDENTIALS
const char* ssid = ""; // ISI PAKE NAMA WIFI
const char* password = ""; // ISI PAKE PASSWORD WIFI

// DOMAIN NAME
const char* serverName = "https://lasti.000webhostapp.com/test.php";

// API KEY
String apiKey = "tPmAT5Ab3j7F9";

// BUTTON
const int switch_button = 4;
int state;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  // INIT BUTTON
  pinMode(switch_button, INPUT);
  // CONNECT WIFI
  WiFi.begin(ssid,password);
  Serial.println("Menyambungkan");
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Tersambung WIFI pada address: ");
  Serial.println(WiFi.localIP());


}

void loop() {
  // put your main code here, to run repeatedly:
  if (WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    // POST IF BUTTON IS PRESSED
    state = digitalRead(switch_button);
    if (state == HIGH){
      String httpRequestData = "api_key=" + apiKey + "&nomeja=" + 6 + "&status=" + "'Terisi'";
      Serial.print("httpRequestData: ");
      Serial.println(httpRequestData);
      int httpResponseCode = http.POST(httpRequestData);
      if (httpResponseCode > 0){
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
      }
      else{
        Serial.print("Error Code: ");
        Serial.println(httpResponseCode);
      }
      delay(2000);
    }
    // POST IF BUTTON IS NOT PRESSED
    else{
      String httpRequestData = "api_key=" + apiKey + "&nomeja=" + 6 + "&status=" + "'Kosong'";
      Serial.print("httpRequestData: ");
      Serial.println(httpRequestData);
      int httpResponseCode = http.POST(httpRequestData);
      if (httpResponseCode > 0){
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
      }
      else{
        Serial.print("Error Code: ");
        Serial.println(httpResponseCode);
      }
      delay(5000);
    }
    http.end();
  }
  else{
    Serial.println("WiFi Disconnected");
  }
}
