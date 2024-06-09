# SolarVault :: The DIY Solar Battery

![logo](https://github.com/carforge/solarvault/assets/29213494/9ef1d83a-3947-496c-854d-47b59f99cea7)
*[AI Generated with Midjourney](https://www.midjourney.com)*

### Background
Ich betreibe Zuhause ein Balkonkraftwerk. Letztendlich nichts anderes, als eine kleine Solaranlage mit einer Leistung von 600Wp (Update auf 800Wp ist schon geplant). Der Solarstrom wird dann einfach über die Steckdose ins Netz eingespeist. Selbst wenn ich von Zuhause aus arbeite, mein Laptop und zwei Bildschirme laufen, produziere ich an sonnigen Tagen oft mehr Strom, als ich verbrauche. Dieser Strom fließt einfach zurück ins Netz und wird nicht vergütet. Zugegeben, es ist nicht viel. Dennoch möchte ich diesen Überschuss speichern um Nachts meine Geräte wie Handys oder Laptops aufzuladen.

### Concept
In einer mehr oder weniger portablen Kiste soll ein Lithium Akku liegen, der mit überschüssigem Solarstrom geladen werden soll. Immer wenn nun die Solaranlage mehr Strom produziert, als ich verbrauche, soll der überschüssige Strom in den Akku gespeichert werden. Dafür verwende ich einen Raspberry Pi, auf dem ein Webserver läuft und welcher per API Spannung und Strom für die Ladung einstellen kann. Dazu wird ein Netzteil mit USB Schnittstelle an dem Raspberry Pi angeschlossen.
