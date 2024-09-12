[CmdletBinding()]
param (
    [Parameter(Mandatory, HelpMessage="Ange ifrån vilket datum du vill schemalägga ifrån i formatet yyyy-MM-dd")]
    [datetime]
    $ScheduleFromDate,

    [ValidateScript({
        if( -Not ($_ | Test-Path) ){
            throw "File: File " +$_ +"does not exist"
        }
        return $true
    })]
    [System.IO.FileInfo]$csvpath = "$PSScriptRoot\$(get-date -Format yyyy-MM-dd) * Ansvarsuppgifter.csv"
)

begin{
    $Exportfile = "$PSScriptRoot\duty-Exportfile-$(get-date -Format yyyy-MM-dd).csv"
    $csv = Import-Csv $csvpath
}

process{
    $arr = foreach ($c in $csv){
        [datetime]$date = $c.Date
        if ($date -ge $ScheduleFromDate){
            [datetime]$midweekDate = $c.Date
            $weekendDate = $date.AddDays(3)
            $midweekDateFormatted = $midweekDate.ToShortDateString() -replace '-', '/'
            $weekendDateFormatted = $weekendDate.ToShortDateString() -replace '-', '/'

            [PSCustomObject]@{
                Date = $midweekDateFormatted
                Person = $c.Person
                Type = $c.Type
                TypeName = $c.TypeName
            }
            [PSCustomObject]@{
                Date = $weekendDateFormatted
                Person = $c.Person
                Type = $c.Type
                TypeName = $c.TypeName
            }
        }
    }
}

end{
    $arr | Export-Csv -Path $Exportfile -Delimiter "," -Force -Encoding utf8
}