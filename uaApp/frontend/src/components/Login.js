import React,{useState} from 'react';

function Login() {
    const [state, setState] = useState({username:"",password:""});
    const [token, setToken] = useState(false)
    const onSubmit =(e)=>{
        e.preventDefault();
        fetch("http://127.0.0.1:8000/api/login/",{
         
            method:"POST",
            headers:{
                "content-type":"application/json",
                "Access-Control-Allow-Origin": "*"
            },
            body:JSON.stringify({...state})
        }).then(r=>r.json()).then(r=>{
            if(r.success){
                // setError(false);
                // props.success();
                setToken(r.token);
                
            }
        }).catch(er=>{
            setError("Login Failed");
        })
    }
    const onInpChange = (e)=>setState({...state,[e.target.name]:e.target.value})
    return (
        <div className="auth-container">
            <h1>Login</h1>
            <input type="text" value={state.username} onChange={onInpChange} name="username"/>
            <input type="password" value={state.password} onChange={onInpChange} name="password" />
            <button type="submit" onClick={onSubmit}> Login</button>
            {token && <p>{token}</p>}
        </div>
    )
}

export default Login
