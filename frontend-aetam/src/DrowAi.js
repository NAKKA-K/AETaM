import React , { Component } from 'react';
//SuperAgentの利用を宣言
import request from 'superagent';

//仮の画像、左から痩せ、普通、肥満
var img=['slim.jpeg','normal.jpg','debu.jpg'];

//画像表示コンポーネント
export default class DrowAi extends Component{
  constructor(props){
    super(props)
    //初期化
    this.state={
      obesity: 0,
      serious: 0,
      hot: 0,
      strong: 0,  
      kind: 0,
    }
  }
  
  //json形式で値を受け取る関数
  getState(){
    //とりあえずテスト用のjsonを使用。public下に置いてる。
     request.get("./test2.json")
            .end((error,res) => {
               if(!error && res.status===200){
                 console.log(res.text)
                 const json=JSON.parse(res.text)
                 this.setState({
                   obesity: json.obesity,
                   serious: json.serious,
                   hot:     json.hot,
                   strong:  json.strong,
                   kind:    json.kind
                 })
               }
               else{
                 console.log(error)
               }
             });
  }

  //マウントされる時
  componentDidMount(){
    setInterval(()=>{this.getState()},1000);
  }

  render(){
    const obesity=this.state.obesity;
    const serious=this.state.serious;
    const hot=this.state.hot;
    const strong=this.state.strong;
    const kind=this.state.kind;
    return(
      <div>
       <label>
         obesity:{obesity}<br/>
         serious:{serious}<br/>
         hot:{hot}<br/>
         strong:{strong}<br/>
         kind:{kind}<br/>
       </label>
       <img src={img[obesity]}/>
      </div>
    ) 
  }
}
