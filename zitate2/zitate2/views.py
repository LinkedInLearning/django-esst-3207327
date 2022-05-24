from django.shortcuts import render
from django.http import HttpResponse
import random


zitate = ("Der Ball ist rund und ein Spiel dauert 90 Minuten! ",
"Der Ball ist rund. Wäre er eckig, wäre er ja ein Würfel. ",
"Wäre, wäre, Fahrradkette ",
"Ich mache nie Voraussagen und werde dies auch niemals tun. ",
"Ich bin körperlich und physisch topfit. ",
"Ich hatte vom Feeling her ein gutes Gefühl. ",
"Wir müssen gewinnen, alles andere ist primär. ",
"Ich habe ihn nur ganz leicht retuschiert. ",
"Fußball ist Ding, Dang, Dong. Es gibt nicht nur Ding. ",
"Am Ergebnis wird sich nicht mehr viel ändern. Es sei denn, es schießt einer ein Tor. ",
"Die schönsten Tore sind diejenigen, bei denen der Ball schön flach oben rein geht. ",
"Wir sind eine gut intrigierte Truppe. ",
"Das habe ich ihm dann auch verbal gesagt. ",
"Zuerst hatten wir kein Glück, und dann kam auch noch Pech dazu. ",
"Ich habe viel von meinem Geld für Alkohol, Weiber und schnelle Autos ausgegeben. Den Rest habe ich einfach verprasst. ",
"Ich bin immer sehr selbstkritisch, auch mir selbst gegenüber. ",
"Struuuunz. Was erlauben Struuuunz? ",
"Mailand oder Madrid – Hauptsache Italien! ",
"Zwei Chancen, ein Tor – das nenne ich hundertprozentige Chancenauswertung. ",
"Man darf jetzt nicht alles so schlecht reden, wie es war. ",
"Das wird alles von den Medien hochsterilisiert. ",
"Man lässt das alles nochmal Paroli laufen. ",
"Wir können so was nicht trainieren, sondern nur üben. ",
"Mal verliert man und mal gewinnen die anderen. ",
"Ich sage nur ein Wort: Vielen Dank! ",
"Ich habe es mir sehr genau überlegt und dann spontan zugesagt. ",
"Da gehe ich mit Ihnen ganz chloroform. ",
"Die Sanitäter haben mir sofort eine Invasion gelegt. ",
"Bei so einem Spiel muß man die Hosen runterlassen und sein wahres Gesicht zeigen. ",
"Das Runde muß ins Eckige. ",
"I hope, we have a little bit lucky. ",
"Es gibt nur eine Möglichkeit: Sieg, Unentschieden oder Niederlage! ",
"Ich habe fertig. ",
"Lebbe geht weida! ",
"Es war die Hand Gottes. ",
"Wir wollten in Bremen kein Gegentor kassieren. Das hat auch bis zum Gegentor ganz gut geklappt. ",
"Es muss eine Kehrtwende geben. Und die muss 360 Grad sein. ",
"Jede Seite hat zwei Medaillen! ",
"Man muss nicht immer die absolute Mehrheit hinter sich haben, manchmal reichen auch 51 Prozent. ",
"Wir waren früher härter; bei uns gab's keine Verletzungen, sondern nur glatte Brüche. ",
"Die wissen nicht einmal, dass im Ball Luft ist. Die glauben doch, der springt, weil ein Frosch drin ist. ",
"Wir müssen vor dem Tor einfach cooler sein, einfach heißer. ",
"Da mach‘ ich mir vom Kopf her keine Gedanken. ",
"Viele sehen es negativ, dass wir schlecht gespielt haben. ")
def index(request):
    index = random.randint(0, len(zitate)-1) 
    
    return HttpResponse(zitate[index])
