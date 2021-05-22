function getInitials(name){
    //  split
    //  concat
     const names = name.split(' ')
     const initials = `${names[0][0]}.${names[1][0]}`;
      return initials
     
    }
    
    console.log(getInitials("Mosharraf Musa"))