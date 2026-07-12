function reverse(s)
{
   let ch=''
    for(i=0;i<s.length;i++)
    {
        ch=s[i]+ch

    }
    

    if(ch===s)
    {
        return"palindrome string"
    }
    else
    {
        return "not pallindrome"
    }
}

console.log(reverse("sreenath"))