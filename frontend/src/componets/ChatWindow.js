import Menu from './Menu.js'
import HistoryChat from './HistoryChat.js'
import InputMassage from './InputMassage.js'

import './style/ChatWindow.css'
import './style/HistoryChat.css'
import './style/InputMassage.css'

import eye from './../assets/eye.png';

function ChatWindow() {
    return (
        <div className="chatWindow">
            <div className="headerChat">
                <div className="headerChat__bot">
                    <img src={eye} alt="eye" />
                    <h2 className="headerChat__bot--title">Name</h2>
                </div>
                <Menu />
            </div>
            <HistoryChat />
            <InputMassage />
        </div>
    );
}

export default ChatWindow;
