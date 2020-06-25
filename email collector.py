def collector(string):
    import re
    pattern = '[a-zA-Z0-9._-]+@+[a-zA-Z]+\.+[A-Za-z]+'
    find = re.findall(pattern,string)
    list = []
    for i in find:
        list.append(i)

    j=1
    f = open("mailid.txt", "w")
    for i in list:
        f.write(f"{j}:{i}\n")
        j+=1
    f.close()

if __name__ == "__main__":
    string = '''Internet email was jatin.rathi@gmail.com designed for 7-bit ASCII.[51] Most email software ruhan.singh@yahoo.com is 8-bit clean,
     but must assume it will communicate with 7-bit servers and mail readers suman.chaudhary@gmail.com . 
     The MIME standard introduced character set kushal.sinha1@hotmail.com specifiers and two content transfer encodings to 
     enable transmission of rockeyman1999@yahoo.com non-ASCII data: quoted printable for mostly 7-bit sohan123@gmail.com content with a few 
     characters outside that range jagan.thakur@hotmail.com and base64 for arbitrary binary data. The 8BITMIME harrybhai@yahoo.com and BINARY 
     extensions were introduced to allow transmission of mail garg.anisha@hotmail.com without the need for these encodings,
      but many mail transport agents may not support them. In some countries, several encoding schemes 
      co-exist; as the result, by default, sharabi.log@gmail.com the message in a non-Latin alphabet language appears in 
      non-readable form sahara.hmara@yahoo.com(the only exception is a coincidence if sushant.rip@yahoo.com the sender and receiver use the same encoding scheme). 
      Therefore, for international character sets, Unicode is growing in popularity.Most modern graphic 
      email clients allow the use of either plain kartik_hamid@hotmail.com text or HTML for the message body at the option of the user. 
      HTML email messages often  include an automatic-generated plain text copy for compatibility. 
      Advantages of HTML include the ability to include in-line links and images, set apart 
      previous messages in block quotes, john.rapper@hotmail.com wrap naturally on any display, use emphasis such as underlines and italics, 
      and change font styles. Disadvantages include the increased size of the email, 
      privacy concerns about web bugs, abuse of HTML email as a vector for phishing attacks 
      and the spread of malicious software.
     Some web-based mailing lists recommend rahul.kutta@yahoo.com all posts be made in plain-text, 
     with 72 or 80 characters per line for all the above reasons, and because they have 
     a significant number of readers using text-based email clients such as Mutt. 
     Some Microsoft email clients may allow rich delhi.gov@gmail.com formatting using their proprietary Rich Text Format (RTF), 
     but this should be avoided unless the recipient is guaranteed to have a compatible email client.'''

    collector(string)
    print("\nSuccessfully extraced all the email ids and saved in the txt file : mailid")
    print("\n\t\tCoded by  Jatin Rathi")
