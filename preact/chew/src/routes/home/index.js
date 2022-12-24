import { h } from 'preact';
import style from './style.css';

import { useState } from 'preact/hooks';


const Home = () => {
	
	const [files, setFiles] = useState([])

	const fetchData = async() => {
		const url = "http://localhost:8000/bubbles/dorky-slobs";
		const headers = {
			method: "GET",
		};
		let response = await fetch(url, headers);
			
		if (response.ok) { // if HTTP-status is 200-299
			let json = await response.json();
			if (json != null){
				console.log(json)
				setFiles(json)
			}

		} 
		else {
			alert("HTTP-Error: " + response.status);
		}
	}
	

	return (<div class={style.home}>
		<h1>Chew</h1>
		<p>Use Chew as a quick, temporary cloud storage.</p>
		<button style={{ color: 'purple' }} onClick={fetchData}>Click me</button>
		<div>
			{
				files.map((file, idx) => (
					<a href={file} download={file} target="_blank">
         					<button type="button">Download file #{idx+1}</button>
         				</a>
				))
			}
		</div>

	</div>)
};

export default Home;
