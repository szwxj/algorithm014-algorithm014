bool isAnagram(char * s, char * t){
    int s1[26],s2[26];
    int i,j;
    for(i=0;i<26;i++){
        s1[i] = s2[i] = 0;
    }

    i = 0;
    while(i<strlen(s)){
        j = s[i] - 'a';
        s1[j] ++; 
        i++;
    }

    i = 0;
    while(i<strlen(t)){
        j = t[i] - 'a';
        s2[j] ++;
        i++;
    }

    for(i = 0;i<26;i++){
        if(s1[i]!=s2[i])
            return false;
    }
    return true;
}