import '../componets/style/MessageUser.css'

let message = "Hola como estas";

function MessageUser() {
    return (
        <div className="ContainerUser">
            <div className="MessageUser">
                <p>{message}</p>
            </div>
        </div>
    );
}

export default MessageUser