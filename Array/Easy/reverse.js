function reverse(s)
{
   let ch=''
    for(i=0;i<s.length;i++)
    {
        ch=s[i]+ch

    }
    return ch
}
console.log(reverse("sreenath"))