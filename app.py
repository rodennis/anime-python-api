from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

db = PostgresqlDatabase('anime', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Facts(BaseModel):
    show_name = CharField()
    fact = CharField(300)

db.connect()
db.drop_tables([Facts])
db.create_tables([Facts])

Facts(show_name = 'naruto', fact = 'Shikamarus IQ is above 200').save()
Facts(show_name = 'naruto', fact = 'Zabuzas name means never cut twice').save()
Facts(show_name = 'naruto', fact = 'Sakura was supposed to die in episdoe 26').save()
Facts(show_name = 'naruto', fact = 'Choujis dad was part of the group that wanted to kill Naruto in Chapter 1.').save()
Facts(show_name = 'naruto', fact = 'Narutos favorite ramen shop Ichiraku exists in real life.').save()
Facts(show_name = 'naruto', fact = 'Shikamarus IQ is above 200.').save()
Facts(show_name = 'naruto', fact = 'Kakuzus techniques are named after the series Mobile Suit Gundam.').save()
Facts(show_name = 'naruto', fact = 'Nejis forehead marks are different in the anime and manga.').save()
Facts(show_name = 'naruto', fact = 'The tallest shinobi in Hidden Leaf is Ibiki Morino').save()
Facts(show_name = 'naruto', fact = 'Sanji from One Piece was supposed to be named Naruto.').save()
Facts(show_name = 'naruto', fact = 'Canonically, Naruto s RasenShuriken is a reddish-orange color.').save()
Facts(show_name = 'naruto', fact = 'Naruto and Kurama s Bijuu Bomb is not the same color as the other bijuus.').save()
Facts(show_name = 'naruto', fact = 'Sarutobi was supposed to be a monkey, but the creator of Naruto changed his mind and make him human like other Shinobis. Maybe that is why lord third was able to summon Enma.').save()

Facts(show_name = 'AOT', fact = 'Hajime Isyama s favorite character is Jean Kirschtein. Cause Isayma admires how Jean says what he wants without worrying about what other people think. But it was all in the past.').save()
Facts(show_name = 'AOT', fact = 'Originally, Eren was going to know that he is a titan all along. But thankfully, Isayama scrapped the idea.').save()
Facts(show_name = 'AOT', fact = 'Levi came on top in the 1st character popularity poll, Eren took the second place, While our favorite girl, Mikasa took the 3rd place.').save()
Facts(show_name = 'AOT', fact = 'Isayama has said that Mikasa will choose not to wear her precious scarf if it s too hot outside.').save()
Facts(show_name = 'AOT', fact = 'Isayama has revealed that Eren s titan form is based on Yushin Okami, a mixed Japanese martial artist. Isayama felt that he had the ideal physique of a middleweight mixed martial artist.').save()
Facts(show_name = 'AOT', fact = 'Moblit is Hange s second in command as well as her assistant. But thats not all. He is also the heaviest drinker in the survey corps. Isayama has said that this is due to his unfortunate position.').save()
Facts(show_name = 'AOT', fact = 'Marnia Inoue, the voice actor of Armin, is also the voice of the show s narrator.').save()
Facts(show_name = 'AOT', fact = 'Mikasa translates to 3 bamboo hats.').save()
Facts(show_name = 'AOT', fact = 'Isayama has said he received a strange phone call from his following the success of his series. They were curious about the sudden increase of funds in his savings. He postulated they probably thought I was running some bank transfer scam.').save()
Facts(show_name = 'AOT', fact = 'Armin s Birthday is on November 3rd, and It suits him. Cause in Japan, The day is celebrated as culture day, promoting academics, culture, and the fine arts.').save()
Facts(show_name = 'AOT', fact = 'Isayama made the theme of AOT cause he thought, Giants are kind of Gross.').save()
Facts(show_name = 'AOT', fact = 'In the Simpsons episode Treehouse of Horror xxv, Lisa was shown dressed as Mikasa. She even used 3D Maneuver Gear.').save()
Facts(show_name = 'AOT', fact = 'Mike is the tallest human character in the series at a looming 6.5.').save()
Facts(show_name = 'AOT', fact = 'It is most likely possible that Erwin Rommel, known as Desert Fox, was served as the main source of inspiration for Erwin Smith.').save()
Facts(show_name = 'AOT', fact = 'Aspects of Levi s design and personality are were based on Rorshach from Watchmen.').save()
Facts(show_name = 'AOT', fact = 'On average, Levi only sleeps around 2 to 3 hours a day.').save()
Facts(show_name = 'AOT', fact = 'Some titans are modeled after friends and acquaintances of Isayama. Sometimes he even takes requests.').save()
Facts(show_name = 'AOT', fact = 'Eren has the highest kill rate of any of the 104 Trainee squad.').save()
Facts(show_name = 'AOT', fact = 'Eren s voice actor Yuki Kaji cried while reading the script of the final season.').save()
Facts(show_name = 'AOT', fact = 'According to Isayama, Erwin stays single because he doesn t know when he ll die. Lucky for the Nile because they were in love with the same woman.').save()
Facts(show_name = 'AOT', fact = 'Isayama revealed that Levi sometimes wishes that he was a bit taller.').save()
Facts(show_name = 'AOT', fact = 'Attack On Titan has 7 episodes rated 9.9 or above. While Breaking Bad and Game Of Thrones have 7 combined.').save()
Facts(show_name = 'AOT', fact = 'Mikasa was the first character Isayama came up with when he was initially developing Attack On Titan.').save()
Facts(show_name = 'AOT', fact = 'Based on statistics from Attack On Titan guide book, Hange and Zeke are the two smartest characters in the series.').save()
Facts(show_name = 'AOT', fact = 'Levi is a Tea enthusiast. He enjoys collecting Tea leaves and is fond of black tea. Isayama has even said that Levi once wanted to open aea shop.').save()
  
Facts(show_name = 'hunterXhunter', fact = 'The words on Zeno Zoldyk s clothing say either A Kill A Day or Never Retire').save()
Facts(show_name = 'hunterXhunter', fact = 'The Phantom Troupe has an arm wrestling rank among themselves to determine their physical strength. The order from strongest to weakest of this arm wrestling is Uvogin, Phinks, Hisoka, Franklin, Feitan, Machi, Chrollo, Bonolenov, Nobunaga, Shalnark, Pakunoda, Shizuku, and Kortopi.').save()
Facts(show_name = 'hunterXhunter', fact = 'All four main protagonists share the same birthday characteristics â€“ having the same number of birth month and day. And coincidentally, Hisoka too shares the same birthday characteristic. This is the reason why some fans consider him as the fifth protagonist.').save()
Facts(show_name = 'hunterXhunter', fact = 'A character from Yu Yu Hakusho, Suzaku appeared in Chrollo s book as one of his victims.').save()
Facts(show_name = 'hunterXhunter', fact = '60 out of the 100 Richest characters in the series are Hunters.').save()
Facts(show_name = 'hunterXhunter', fact = 'The very first character to have appeared in Hunter x Hunter Manga is Kite.').save()
Facts(show_name = 'hunterXhunter', fact = 'Knuckle, Shoot, Palm, and Gyro are named after different baseball pitches Knuckleball, Shoot Ball, Palm ball, and Gyroball.').save()
Facts(show_name = 'hunterXhunter', fact = 'Sui Ishida, the creator of Tokyo Ghoul, is a big fan of Hunter X Hunter. Especially Hisoka.').save()
Facts(show_name = 'hunterXhunter', fact = 'In 1999 Hunter x Hunter anime, Killua watched porno during his stay in a Yorknew City hotel. He even asked Gon to join him. Thankfully, Gon refused the offer.').save()
Facts(show_name = 'hunterXhunter', fact = 'Togashi is married to the author of Sailor Moon, Naoko Takeuchi. She even helped him in earlier chapters.').save()
Facts(show_name = 'hunterXhunter', fact = 'Kurapika is the only known character in the entire HxH series with two Nen types â€“ Conjuration and Specialization.').save()
Facts(show_name = 'hunterXhunter', fact = 'Morel s technique Deep Turtle is a reference to the rock band of the same name.').save()
Facts(show_name = 'hunterXhunter', fact = 'With a 3,250 feet tall,251 floors, Heavens Arena is the 4th tallest building in the Hunter x Hunter series.').save()
Facts(show_name = 'hunterXhunter', fact = 'Hunter x Hunter has its own alphabets which can be translated directly to Japanese then to English.').save()
Facts(show_name = 'hunterXhunter', fact = 'Dwun s room in greed island arc is a reference to a photo of the author s room. Togashi has similar seas of Trash scattered around him while playing the game Dragon Quest.').save()
Facts(show_name = 'hunterXhunter', fact = 'It is shown in the series that Pituo has the biggest En range extending up to 2.2 Kilometers.').save()
Facts(show_name = 'hunterXhunter', fact = 'Killua s favorite food is ChocoRobo-Kun chocolate balls and he hates red peppers. He also has a gambling addiction.').save()
Facts(show_name = 'hunterXhunter', fact = 'Our bald Ninja, Hanzo, is named after Hatori Hanzo, a famous Japanese ninja.').save()
Facts(show_name = 'hunterXhunter', fact = 'Gon shares the same birthday with Monkey D. Luffy, the main protagonist of One Piece.').save()
Facts(show_name = 'hunterXhunter', fact = 'Only Ging Freecss passed the 267th Hunter Examination and it was the same case with Killua but on 288th.').save()
Facts(show_name = 'hunterXhunter', fact = 'Despite his appearances, Kalluto is a boy and is the youngest member of Phantom Troupe.').save()
Facts(show_name = 'hunterXhunter', fact = 'The Greed Island arc is created out of Togashi s desire to draw a card battle manga like Yugioh.').save()
Facts(show_name = 'hunterXhunter', fact = 'Hina s hat imitates her emotions.').save()
Facts(show_name = 'hunterXhunter', fact = 'All Silver-haired members of the Zoldyck family (Zeno, Silva, and Killua) have transmutation type of Nen. On the other hand, the dark-haired members of their family use the Manipulation type.').save()
Facts(show_name = 'hunterXhunter', fact = 'Did you know? Bungee gum has properties of both rubber and gum.').save()


@app.route('/facts', methods=['GET'])
def naruto():
    facts = []
    for fact in Facts:
        facts.append(model_to_dict(fact))
    return jsonify(facts)

app.run(port=3000, debug=True)