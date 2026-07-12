function vowel(s)
{
     let count=0
     for(let ch of s)
     {
        if(ch=='a'|| ch=='e' || ch=='i'|| ch=='o'|| ch=='u'|| ch=='A'|| ch=='E'|| ch=='I'|| ch=='O'|| ch=='U' )
        {
            count++
        }
     }
     console.log(count)
    
}
vowel("sreenath")