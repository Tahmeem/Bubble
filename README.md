# Bubble

## About
Bubble is an easy-to-use discord bot made for customers to recieve details about a business fast and through a bot direct message.
Businesses are also able to send out their latest news and support pages very fast without the hassle of setting up emails. This allows 
for customers to receive information on a business instantly and with bubble's engaging embed messages.

## Why
Bubble is able to send messages fast to 100s of customers with one command making the interaction between customers and a business
much more efficient and fast. Bubble is also able to make messages more engaging with the embeds it sends out in direct messages.

## Features
### !image
!image is a command for bubble to send out an image in jpeg or png to a list of customers on discord. To use it first upload the csv with the list of discord names and type into the textfield !image and then your message in quotes. Bubble will prompt you for a picture is jpeg or png and uploading that picture will send out the dms. This can be used for various things in a business such as quotes from brokers in a picture, sending out big announcements to current customers, or sending adverts for a new deal.
![imageSetUp](Website/images/imageSetUp.png)
![imageDM](Website/images/!imageDM.png)

Command: `!image "add footer here"`

### !contacts
Bubble has this feature to improve customer service. With !contact and a csv file with list of customers, bubble will ask for name, email address and phone number for customer service. Then it will send a direct message with an embed that contains those fields and a link to the company website contact page for more details.
![contactsSetup](Website/images/contactsDemo.PNG)
![contactsDM](Website/images/contactsDM.PNG)

Command: `!contacts`

### !website
This feature is made for new customers that will receive a small description of the company and a link to the company website when !website is sent out with a csv file of the list of customers.
![websiteSetup](Website/images/WebsiteDemo.PNG)
![websiteDM](Website/images/websiteDM.PNG)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install discord.

```bash
pip install discord.py
```
