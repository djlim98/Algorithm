function solution(genres, plays) {
    var answer = [];
    const table={};
    const p_table={};
    for (let i=0; i<genres.length;i++){
        table[genres[i]]=(table[genres[i]]|0)+plays[i];
        p_table[genres[i]]=p_table[genres[i]]||[];
        p_table[genres[i]].push([i,plays[i]]);
    }
    const sortable=[];
    for (let g in table) {
        sortable.push([g, table[g]]);
    }   

    sortable.sort(function(a, b) {
        return b[1] - a[1];
    });
    for(let i=0;i<sortable.length;i++){
        const g=sortable[i][0];
        p_table[g].sort((a,b)=>{
            return b[1] - a[1];
        });
       
        const temp=[];
        while(p_table[g].length!==0&&temp.length<2){
            temp.push(p_table[g].shift());
        }
        
        while(temp.length>0){
            answer.push(temp.shift()[0]);
        }
    };
  
    return answer;
}

//https://programmers.co.kr/learn/courses/30/lessons/42579
