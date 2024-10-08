# NW Scheduler

Lite små script för att underlätta schemaläggningen.

- [Add-SundayToDuties](#Add-SundayToDuties)
- [Schedule-BaseSchedule](#Schedule-BaseSchedule)

<a id="Add-SundayToDuties"></a>
## Add-SundayToDuties
Om man vill schemalägga per möte och ändå schemalägga per vecka och slippa klicka dubbelt upp, kan man använda sig av export och import funktionen tillsammans med skriptet.

Skriptet tar exporten av schemalagd veckomöte och lägger till samma schema för helgmötet.

1. Schemalägg veckomötet i NW Scheduler
2. Exportera duties till samma sökväg som skriptfilen ligger i
3. Kör skriptet med att ange från vilket datum som ska schemaläggas
``` powershell
.\Add-SundayToDuties.ps1 -ScheduleFromDate 2024-09-26
```
4. En CSV fil skapas i samma sökväg som skriptet som används vid import i NW Scheduler
5. Se till att datumformatet är rätt yyyy/MM/dd i import guiden

### Tips 1
Rad 13 testar filnamnet vilket är på svenska i formatet 'yyyy-MM-dd * Ansvarsuppgifter.csv'. Se till att rad 13 matchar språk och format på filen som exporteras.

### Tips 2
Skriptet är anpassat för möte på torsdagar och söndagar ändra siffran på rad 19 för att ändra antal dagar det är ifrån veckomötet till helgmötet.
``` powershell
19:  [int]$AddDays = 3
```

### Tips 3
Skriptet är anpassat för möte på torsdagar, för att ändra veckomötesdag ändra dagens namn på rad 16
``` powershell
16:  [string]$DayOfWeek = 'Thursday'
```


<a id="Schedule-BaseSchedule"></a>
## Schedule-BaseSchedule
Under utveckling...

Syfte är att om man har ett rullande schema, importera dem direkt färdig schemalagda.

### Tips 1
Skriptet är anpassat för möte på torsdagar, för att ändra veckomötesdag ändra dagens namn på rad 16
``` powershell
17:  [string]$DayOfWeek = 'Thursday'
```
