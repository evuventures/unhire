import React from 'react'
import './Card.css';
import projectIcon from "../components/icons/project-icon.png";
import check from "../components/icons/check.png";
import time from "../components/icons/time.png";
import approval from "../components/icons/approval.png";

function Card({ title, imageURL, description }) {
    return (
        <div className="card">
            <div className="card-container">
                <div className="image-container">
                    <img src={projectIcon} alt={title} />
                </div>
                <div className="card-content">
                    <div className="card-title">
                        <h3>Post a Project</h3>
                    </div>
                    <div className="card-description">
                        <p>Clients submit detailed tasks with deadlines and deliverables</p>
                    </div>
                </div>
            </div>

            <div className="card-container">
                <div className="image-container">
                    <img src={check} alt={title} />
                </div>
                <div className="card-content">
                    <div className="card-title">
                        <h3>Claim & Deliver</h3>
                    </div>
                    <div className="card-description">
                        <p>Freelancers claim tasks and submit drafts before final delivery.</p>
                    </div>
                </div>
            </div>

            <div className="card-container">
                <div className="image-container">
                    <img src={time} alt={title} />
                </div>
                <div className="card-content">
                    <div className="card-title">
                        <h3>Timed Execution</h3>
                    </div>
                    <div className="card-description">
                        <p>Deadlines are enforced. Missed timelines = removal from platform.</p>
                    </div>
                </div>
            </div>

            <div className="card-container">
                <div className="image-container">
                    <img src={approval} alt={title} />
                </div>
                <div className="card-content">
                    <div className="card-title">
                        <h3>Client Approval</h3>
                    </div>
                    <div className="card-description">
                        <p>Clients approve or reject submissions. Rejections reduce freelancer standing.</p>
                    </div>
                </div>
            </div>
        </div>




    );
}

export default Card;
