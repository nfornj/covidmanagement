import requests


district_name_list=['Ernakulam','Kozhikode','Wayanad','Idukki','Malappuram','Thrissur','Pathanamthitta','Thiruvananthapuram','Palakkad','Kottayam','Kollam','Kasaragod','Kannur']


def postmessage(district_name,content):

    print ("hola")

    if district_name=="india":
         r= requests.post("https://api.telegram.org/bot1813237434:AAF3-HAA9Rhklz0v2T73p6-GhUxQuNfoBWU/sendMessage?chat_id=@india_vaccine_availability&text="+content+"&parse_mode=html")
        
         print (r.text)
    else:
        r= requests.post("https://api.telegram.org/bot1813237434:AAF3-HAA9Rhklz0v2T73p6-GhUxQuNfoBWU/sendMessage?chat_id=@"+district_name+"_covid_vaccine_updates&text="+content+"&parse_mode=html")
        print (r.text)       



def sendmessage(df,age):


    if not df.empty:
        
        print (df['district_name'].iloc[0])

        content="<b>District : </b>"+df['district_name'].iloc[0]+"\t\t\t<b>Age Limit : "+str(age)+"</b>\n"

        for index, row in df.iterrows():
            print (row['name'])
            
            content=content+"\n<b>Pin : </b>"+str(int(row['pincode']))+"\n<b>Vaccine Date : </b>"+row['vaccine_date']+"\t<b>Vaccine : </b>"+row['vaccine']+"\n<b>Hospital Name : </b>"+row['name']+"\n<b>Availability : </b>"+str(row['available_capacity'])+"\t\t\t<b>Dose1 : </b>"+str(int(row['available_capacity_dose1']))+"\t<b>Dose2 : </b>"+str(int(row['available_capacity_dose2'])) + "\n<b>FeeType : </b>"+str(row['fee_type'])+"\n"
            content = content + "_________________________________\n"
            
            if len(content)>=3800:
            
                content = content + "<b>Book: </b>https://selfregistration.cowin.gov.in \n"
            
                if df['district_name'].iloc[0] in district_name_list:
                    content = content + str(df['district_name'].iloc[0]) + " Channel : \n https://t.me/"+str(df['district_name'].iloc[0])+"_covid_vaccine_updates"

                    postmessage(str(df['district_name'].iloc[0]),content)
                    postmessage("india",content)

                    content="<b>District : </b>"+df['district_name'].iloc[0]+"\t\t\t<b>Age Limit : "+str(age)+"</b>\n"
                 
  
        
        print (content)
        content = content + "<b>Book: </b>https://selfregistration.cowin.gov.in \n"
        content = content + str(df['district_name'].iloc[0]) + " Channel : \n https://t.me/"+str(df['district_name'].iloc[0])+"_covid_vaccine_updates"
         
        postmessage("india",content)
        
        if df['district_name'].iloc[0] in district_name_list:
            
            postmessage(str(df['district_name'].iloc[0]),content)
           
