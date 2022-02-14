import React, { useRef } from "react";

import menuIcon from './../assets/menuIcon.png';
import logo from './../assets/logo.png';
import backMenu from './../assets/backMenu.png';

import './style/menu.css'

function Menu() {
    let refMenuBlock = useRef();

    const handleToggleMenu = () => {
        refMenuBlock.current.classList.remove("none");
    }
    const actionBackMenu = () => {
        refMenuBlock.current.classList.add("none");
    }
    
    return (
        <div className="menu">
            <img id="menuIcon" className="menuIcon" onClick={handleToggleMenu} src={menuIcon} alt="menu" />
            <div ref={refMenuBlock} className="detailsMenu none">
                <div className="detailsMenu__header">
                    <img src={logo} alt="Caif" />
                </div>
                <ul>
                    <li type="disc">Chat</li>
                    <li type="disc">Text generator</li>
                </ul>
                <div className="detailsMenu__footer">
                    <img onClick={actionBackMenu} src={backMenu} className="backMenu" alt="back" />
                    <button>Login</button>
                </div>
            </div>
        </div>
    );
}

export default Menu;