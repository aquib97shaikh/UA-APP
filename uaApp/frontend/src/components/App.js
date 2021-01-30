import React,{useState} from 'react'
import Login from './Login'
import Signup from './Signup'
import Tab from './Tab';

function App() {
    const [loginShow, setLoginShow] = useState(true);
    const tabHandler = (a)=>{
        console.log({a});
        a===0 ? setLoginShow(true) : setLoginShow(false);
    }

    return (
        <div>
            <Tab options={["Login","Signup"]} tabHandler={tabHandler}/>
            {loginShow ? <Login  /> : <Signup/>}
        </div>
    )
    // const [login, setLogin] = useState(true)
    // return (
    //     <div>
    //         <Tab ></Tab>
    //         {login ? <Login /> :<Signup />}
    //     </div>
    // )
}

export default App
