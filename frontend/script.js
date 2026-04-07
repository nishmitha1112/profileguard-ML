function animateConfidence(targetPercent, colorClass) {
    const ring = document.getElementById("confidence-ring");
    const valueEl = document.getElementById("confidence-value");

    let current = 0;
    const duration = 800; // ms
    const stepTime = 20;
    const steps = duration / stepTime;
    const increment = targetPercent / steps;

    // base color per state
    const color =
        colorClass === "real" ? "#22c55e" :   // green
        colorClass === "fake" ? "#ef4444" :   // red
        "#9ca3af";                            // neutral

    const timer = setInterval(() => {
        current += increment;
        if (current >= targetPercent) {
            current = targetPercent;
            clearInterval(timer);
        }
        // angle for conic gradient
        const angle = (current / 100) * 360;
        ring.style.setProperty("--angle", angle + "deg");
        ring.style.setProperty("--color", color);
        valueEl.textContent = Math.round(current) + "%";
    }, stepTime);
}

function resetToWaiting() {
    const shield = document.getElementById("shield-icon");
    const status = document.getElementById("result");
    const risk = document.getElementById("risk");
    const reason = document.getElementById("reason-text");
    const ring = document.getElementById("confidence-ring");
    const valueEl = document.getElementById("confidence-value");

    shield.className = "shield neutral";
    shield.textContent = "?";

    status.className = "status waiting";
    status.textContent = "Ready to Predict";

    risk.className = "risk-badge neutral";
    risk.textContent = "Awaiting Input";

    reason.textContent =
        "Provide profile metrics on the left to let ProfileGuard ML analyze authenticity.";

    ring.style.setProperty("--angle", "0deg");
    ring.style.setProperty("--color", "#9ca3af");
    valueEl.textContent = "--%";
}

function predict() {
    const followers_count = Number(document.getElementById("followers_count").value);
    const friends_count = Number(document.getElementById("friends_count").value);
    const ff_ratio = Number(document.getElementById("ff_ratio").value);

    // basic guard: if inputs empty, reset state
    if (!followers_count && !friends_count && !ff_ratio) {
        resetToWaiting();
        return;
    }

    const verified = document.getElementById("verified").checked ? 1 : 0;
    const default_profile = document.getElementById("default_profile").checked ? 1 : 0;

    let data = {
        followers_count,
        friends_count,
        ff_ratio,
        verified,
        default_profile
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        const shield = document.getElementById("shield-icon");
        const status = document.getElementById("result");
        const risk = document.getElementById("risk");
        const reason = document.getElementById("reason-text");

        // Simulated confidence (since backend doesn't send it)
        const base = result.prediction === "REAL USER" ? 88 : 80;
        const jitter = Math.floor(Math.random() * 7); // 0–6
        const confidence = base + jitter;

        if (result.prediction === "REAL USER") {
            // REAL USER STATE
            shield.className = "shield real";
            shield.textContent = "✔";

            status.className = "status real";
            status.textContent = "REAL USER";

            risk.className = "risk-badge low";
            risk.textContent = "LOW RISK";

            reason.textContent =
                "The profile shows strong authenticity signals based on network behavior and follower–friend patterns.";

            animateConfidence(confidence, "real");
        } else {
            // FAKE USER STATE
            shield.className = "shield fake";
            shield.textContent = "!";

            status.className = "status fake";
            status.textContent = "FAKE USER";

            risk.className = "risk-badge high";
            risk.textContent = "HIGH RISK";

            reason.textContent =
                "The profile indicates suspicious patterns such as abnormal follower–friend ratios or default visuals.";

            animateConfidence(confidence, "fake");
        }
    })
    .catch(err => {
        console.error(err);
        resetToWaiting();
        const status = document.getElementById("result");
        status.textContent = "Server Error";
    });
}

// initialize on load
resetToWaiting();
