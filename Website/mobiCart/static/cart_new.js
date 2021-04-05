var total=0;
var items=["airpods","airpodspro","bspeakers","covers"];
var itemcount=[0,0,0,0];
var itemprice=[18900.0,24900.0]
function cartload()
{
    if(total==0)
    {

        document.getElementById("tot").innerHTML="Total items in cart:0";
        var row=document.getElementById("mytable").insertRow(-1);
        var cell1=row.insertCell(0);
        var cell2=row.insertCell(1);
        var cell3=row.insertCell(2);
        var cell4=row.insertCell(3);
        cell1.innerHTML="None";
        cell2.innerHTML=0.0;
        cell3.innerHTML=0;
        cell4.innerHTML=0.0;
    }
}
function addcart(item)
{


    if(item==items[0])
    {
        itemcount[0]++;
        total++;
        document.getElementById("tot").innerHTML="Total items in cart:"+total;
        var row=document.getElementById("mytable").insertRow(-1);
        var cell1=row.insertCell(0);
        var cell2=row.insertCell(1);
        var cell3=row.insertCell(2);
        var cell4=row.insertCell(3);
        cell1.innerHTML=items[0];
        cell2.innerHTML=itemprice[0];
        cell3.innerHTML=itemcount[0];
        cell4.innerHTML=itemcount[0]*itemprice[0];


    }
    else if(item==items[1])
    {
        itemcount[1]++;
        total++;
        document.getElementById("tot").innerHTML="Total items in cart:"+total;
        var row=document.getElementById("mytable").insertRow(-1);
        var cell1=row.insertCell(0);
        var cell2=row.insertCell(1);
        var cell3=row.insertCell(2);
        var cell4=row.insertCell(3);
        cell1.innerHTML=items[1];
        cell2.innerHTML=itemprice[1];
        cell3.innerHTML=itemcount[1];
        cell4.innerHTML=itemcount[1]*itemprice[1];


    }
}
function deleteItem()
{
}
cartload();