# 🤡 Telegram Phone Scraper 🤡
<pre>
                        .=*%@@@@@@@@%*:             
                       :%@@@@@@@@@%##%@**+:          
                      -@@@@@@@@@%=   -@@@@@=         
                      %@@@@@@@@@:    +@@@@@*        
                     :@@@@@@@@@+      +%@%+.        
                     =@@@@@@@@@+           
                     +@@@@@@@@@@:           
                     *@@@@@@@@@@%:         
    .-+*#%%##*+=:.   #@@@@@@@@@@@#    .:----:.         
  :*@@@@@@@@@@@@@@#=.@@@@@@@@@@@@@:.=#@@@@@@@@%#+:  
 -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=%@@@@@@@@@@@@@@#= 
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
 @@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
 %@@@@@+   .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+==+%@@@@@-
 -@@@@%      =@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.     -%@@@-
  :#@@@-      =@@@@@@@@@@@@@@@@@@@@@@@@@@+       -*@@#
    -#@@%#=    +@@@@@@%#%@@@@@@@%#%@@@@@*       *@@@@@:
     #@@@@@-    #@@@%-   .=%@%=.   -%@@@.       #@@@@@-
     *@@@@@-    :@@%.       :       .%@%        .*%%#=
      -**+:      #@=                 =@%         
                 #@.                 .@#     
                 *@.                 .@#     
                 *@.                  .@*    
                 +@:                 .@+  
                 -@:                 :@-
                  %=                 =%  
                  =%:               :%-   
                   #%              -%#  
                   :%%=            %%.  
                    :#%           %#:  
                     .=%+.     .+%=      
                       .=##=:=*#-  
                          #@@@+  
</pre>          

This bot collects public phone numbers from Telegram groups and organizes them by country.

## 👁️‍🗨️Features
🔻 Automatically collects phone numbers  
🔻 Sorts numbers by country  
🔻 Saves data to a file on the desktop  

## **👁️‍🗨️ How does the bot work?**
🔺 **On the first run**, the bot will ask you to enter **API_ID, API_HASH, and PHONE_NUMBER** (these are required for the Telegram API).  
🔺 **You confirm login** – the bot will be added as a new device to your Telegram account.  
🔺 **The bot waits for you to send any message in the target group** where you want to collect numbers.  
   - This message can be **a dot (`.`), a letter, a number, or any other symbol**.  
   - After this, the bot understands **which chat it should collect numbers from**.  
🔺 **The bot scans the group and extracts data:**  
   - 🔍 **Total profiles scanned**  
   - 📞 **Users with visible phone numbers**  
   - 🚫 **Users without phone numbers**  
🔺 **The final file is saved on your desktop** with the name of the group.

## 👁️‍🗨️Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/wrtgn/telegram-phone-scraper.git
   cd telegram-phone-scraper
2. Install dependencies: 
    ```bash
    pip install -r requirements.txt
3. Run the bot:
    ```bash
   python telegram-phone-scraper.py
