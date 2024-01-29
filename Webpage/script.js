// Function to get browser information
function getBrowserInfo() {
    const navigatorInfo = `
        <p>Navigator:</p>
        <ul>
            <li>appName: ${navigator.appName}</li>
            <li>product: ${navigator.product}</li>
            <li>appVersion: ${navigator.appVersion}</li>
            <li>userAgent: ${navigator.userAgent}</li>
            <li>platform: ${navigator.platform}</li>
            <li>language: ${navigator.language}</li>
        </ul>
    `;

    const windowInfo = `
        <p>Window:</p>
        <ul>
            <li>innerHeight: ${window.innerHeight}</li>
            <li>innerWidth: ${window.innerWidth}</li>
        </ul>
    `;

    const screenInfo = `
        <p>Screen:</p>
        <ul>
            <li>width: ${screen.width}</li>
            <li>height: ${screen.height}</li>
            <li>availWidth: ${screen.availWidth}</li>
            <li>availHeight: ${screen.availHeight}</li>
            <li>colorDepth: ${screen.colorDepth}</li>
            <li>pixelDepth: ${screen.pixelDepth}</li>
        </ul>
    `;

    const locationInfo = `
        <p>Location:</p>
        <ul>
            <li>href: ${window.location.href}</li>
            <li>hostname: ${window.location.hostname}</li>
            <li>pathname: ${window.location.pathname}</li>
            <li>protocol: ${window.location.protocol}</li>
        </ul>
    `;

    let geolocationInfo = "<p>Geolocation:</p>";
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            geolocationInfo += `
                <ul>
                    <li>Latitude: ${position.coords.latitude}</li>
                    <li>Longitude: ${position.coords.longitude}</li>
                </ul>
            `;
            document.getElementById("browser-info").innerHTML = navigatorInfo + windowInfo + screenInfo + locationInfo + geolocationInfo;
        }, error => {
            geolocationInfo += `<p>Error retrieving geolocation information: ${error.message}</p>`;
            document.getElementById("browser-info").innerHTML = navigatorInfo + windowInfo + screenInfo + locationInfo + geolocationInfo;
        });
    } else {
        geolocationInfo += "<p>Geolocation is not supported in this browser.</p>";
        document.getElementById("browser-info").innerHTML = navigatorInfo + windowInfo + screenInfo + locationInfo + geolocationInfo;
    }
}

// Call the function to get and display browser information
getBrowserInfo();

document.getElementById("developer-description").addEventListener("click", showDeveloperDescription);
document.getElementById("contact-me").addEventListener("click", showContactMe);

function showDeveloperDescription() {
    hideAllContent();
    document.querySelector(".developer-description-content").style.display = "block";
}

function showContactMe() {
    hideAllContent();
    document.querySelector(".contact-me-content").style.display = "block";
}

function hideAllContent() {
    document.querySelector(".developer-description-content").style.display = "none";
    document.querySelector(".contact-me-content").style.display = "none";
}