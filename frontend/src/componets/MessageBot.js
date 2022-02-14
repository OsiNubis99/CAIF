import '../componets/style/MessageBot.css'


let message = "Hola como estas";

function MessageBot() { 
    return (
        <div className="ContainerBot">
            <div className="MessageBot">
                <p>{message}</p>
            </div>
        </div>
    );
}

export default MessageBot