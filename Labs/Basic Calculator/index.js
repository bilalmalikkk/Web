obj = document.getElementById("output");
for(i of document.querySelectorAll('.number'))
{
    i.addEventListener
    ('click', function(e)
    {
        if(e.target.innerText === "=")
        {
            obj.value = eval(obj.value);
        }
        else if(e.innerText==="CE")
        {
            obj.value="";
        }
        else if(e.target.innerText === "C")
        {
           obj.value = "";
        }
        else
        {
            obj.value = obj.value + e.target.innerText;
        }
    })
}
function factorial()
{
    numb = obj.value
    if(numb === 0){
        obj.value = 1;
    }
    else{
        res = 1;
        while(numb > 1){
            res = res * numb;
            numb = numb - 1;
        }
        obj.value = res;
    }
}

function power()
{
    po=obj.val;
    if(po!="")
    {
        obj.value = Math.pow(2,obj.value);
    }       
}
function log2()
{
    obj.value = Math.log2(obj.value)
}
function log10()
{
    obj.value = Math.log10(obj.value)
}
function PI()
{
    obj.value = 3.1416;
}

function sqrt()
{
    obj.value = Math.sqrt(obj.value);
}
function sin()
{
    obj.value = Math.sin(obj.value)
}
function cos()
{
   obj.value = Math.cos(obj.value)
}
function tan()
{
    obj.value = Math.tan(obj.value)
}
function percentage()
{
    obj.value = obj.value / 100;
}






