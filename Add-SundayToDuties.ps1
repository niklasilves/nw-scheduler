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
    [int]$AddDays = 3
}

process{
    $arr = foreach ($c in $csv){
        [datetime]$midweekDate = $c.Date
        if ($midweekDate -ge $ScheduleFromDate){
            [PSCustomObject]@{
                Date = $midweekDate.ToShortDateString() -replace '-', '/'
                Person = $c.Person
                Type = $c.Type
                TypeName = $c.TypeName
            }
            [PSCustomObject]@{
                Date = $midweekDate.AddDays($AddDays).ToShortDateString() -replace '-', '/'
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