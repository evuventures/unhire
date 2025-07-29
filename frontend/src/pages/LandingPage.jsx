import React from 'react';
import './landingPage.css';

const LandingPage = () => {
    return (
        <div className="container">
            <header className="header">
                <h1 className="title">Unhire</h1>
                <p className="subtitle">
                    The freelance platform that guarantees delivery. No missed deadlines. No excuses.
                </p>
                <button className="join-button">Join Waitlist</button>
            </header>


            <section className="how-it-works">
                <h2>How It Works</h2>
                <div className="steps">
                    <div className="step">
                        <img src="icon1.png" alt="Post a Project" className="icon" />
                        <h3>Post a Project</h3>
                        <p>Clients submit detailed tasks with deadlines and deliverables.</p>
                    </div>
                    <div className="step">
                        <img src="icon2.png" alt="Claim & Deliver" className="icon" />
                        <h3>Claim & Deliver</h3>
                        <p>Freelancers claim tasks and submit drafts before final delivery.</p>
                    </div>
                    <div className="step">
                        <img src="icon3.png" alt="Timed Execution" className="icon" />
                        <h3>Timed Execution</h3>
                        <p>Deadlines are enforced. Missed timelines = removal from platform.</p>
                    </div>
                    <div className="step">
                        <img src="icon4.png" alt="Client Approval" className="icon" />
                        <h3>Client Approval</h3>
                        <p>Clients approve or reject submissions. Rejections reduce freelancer standing.</p>
                    </div>
                </div>
            </section>

            <section className="why-unhire">
                <h2>Why Unhire</h2>
                <div className="steps">
                    <div className="step">
                        <img src="icon1.png" alt="Post a Project" className="icon" />
                        <h3>No Bidding Wars</h3>
                        <p>Freelancers claim tasks directly without endless back-and-forth</p>
                    </div>
                    <div className="Quality Over Quantity">
                        <img src="icon2.png" alt="Claim & Deliver" className="icon" />
                        <h3></h3>
                        <p>We vet every freelancers and remove those who underperform</p>
                    </div>
                    <div className="Transparent-Workflow">
                        <img src="icon3.png" alt="Timed Execution" className="icon" />
                        <h3>Transparent Workflow</h3>
                        <p>Clients and freelancers share a real-time dashboard and project timeline</p>
                    </div>

                </div>
            </section>
        </div>
    )
}
export default LandingPage;
