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
    [System.IO.FileInfo]
    $csvpath = "$PSScriptRoot\base_schedule.csv"
)

begin{
    $Exportfile = "$PSScriptRoot\duty-BaseImport-$(get-date -Format yyyy-MM-dd).csv"
    $csv = Import-Csv $csvpath 
    $group = $csv | Group-Object date
}

process{
    [datetime]$Date = $ScheduleFromDate
    $arr = foreach ($grp in $group){
        foreach ($g in $grp.Group){
            [PSCustomObject]@{
                Date = $Date.ToShortDateString()
                Person = $g.Person
                Type = $g.Type
                TypeName = $g.TypeName
            }
        }
        $Date = $Date.AddDays(7)
    }
}

end{
    $arr | Export-Csv -Path $Exportfile -Delimiter "," -Force -Encoding utf8
}