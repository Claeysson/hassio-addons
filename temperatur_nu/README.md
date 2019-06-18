## Temperatur.nu reporter add-on för HASS.IO

Denna add-on rapporterar din aktuella temperatur regelbundet till [temperatur.nu](http://temperatur.nu). För att kunna rapportera temperatur till temperatur.nu krävs att du är [registrerad](http://wiki.temperatur.nu/index.php/Rapportera_till_temperatur.nu) som rapportör. För att bli detta behöver du lämna in en [intresseanmälan](https://www.temperatur.nu/nystation/).

### Krav som ställs från temperatur.nu

* Temperatur.nu **skall** få tillgång till temperaturen dygnet runt. Temperaturen du rapporterar **skall** vara skuggtemperaturen. Det är lämpligt att mäta och rapportera temperaturen från två väderstreck så minskar risken för problem med solinstrålning.
* Temperaturen bör ha en upplösning på 0,1 grader.
* Temperaturen bör uppdateras var femte minut eller oftare.

### Konfiguration

Följande parametrar måste anges innan detta add-on kan startas. Om någon av dessa parametrar saknas eller är felaktigt formaterad kommer en felbeskrivning att anges.

| Parameter | Beskrivning                                                  |
| :-------- | :----------------------------------------------------------- |
| hash      | Den unika kod som angivits av temperatur.nu för att identifiera din position. |
| entity    | Din termometers entitet.                                     |
| interval  | Hur ofta temperaturen skall rapporteras angivit i sekunder.  |

### Problem

Vid problem med tjänsten kontakta [temperatur.nu](https://www.temperatur.nu/kontakta.html).

Vid problem med detta add-on skapa ett ärende på [GitHub](https://github.com/Claeysson/addon-temperatur_nu/issues).