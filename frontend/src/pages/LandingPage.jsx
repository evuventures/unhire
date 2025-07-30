import React from 'react';
import './landingPage.css';
import Card from './Card';

const LandingPage = () => {
    return (
        <>
            <div className="container">
                <header className="header">
                    <h1 className="title">Unhire</h1>
                    <p className="subtitle">
                        The freelance platform that guarantees delivery. No missed deadlines. No excuses.
                    </p>
                    <button className="join-button">Join Waitlist</button>
                </header>
            </div>

            <div>
                <section className="how-it-works">
                    <h2>How It Works</h2>
                    <div className="cards-container">
                        <Card />
                    </div>
                </section>

                <section className="why-unhire">

                    <h2>Why Unhire?</h2>

                    <div className="unhire-features">
                        <div className="feature">
                            <h3>No Bidding Wars</h3>
                            <p>Freelancers claim tasks directly without endless back-and-forth</p>
                        </div>
                        <div className="feature">
                            <h3>Quality Over Quantity</h3>
                            <p>We vet every freelancer and remove those who underperform.</p>
                        </div>
                        <div className="feature">
                            <h3>Transparent Workflow</h3>
                            <p>Clients and freelancers share real-time dashboard and project timeline.</p>
                        </div>
                    </div>
                </section>
            </div>
        </>
    );
}


export default LandingPage;
