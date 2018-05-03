package projects.Collect.nodes.timers;

import projects.Collect.nodes.messages.DataMessage;
import projects.Collect.nodes.nodeImplementations.GAF;
import projects.Collect.nodes.nodeImplementations.GAF.States;
import projects.Collect.nodes.nodeImplementations.Sink;
import sinalgo.nodes.timers.Timer;
import sinalgo.runtime.Global;

public class TaTimer extends Timer {

	/**
	 * The instance of the node that call the timer
	 */
	public GAF gaf;
	
	public TaTimer(GAF gaf) {
		
		this.gaf = gaf;
	}

	@Override
	public void fire() {
				
		if(this.gaf.state == States.active) {
			
			int idMessage = Integer.parseInt(this.gaf.ID + "" + this.gaf.dataPctSent++);
			
			if(this.gaf.hasEnergy()) {
				this.gaf.dataPctsSentByHour++;
				Sink.pcktsSentByNetwork++;
				DataMessage msg = new DataMessage(this.gaf.ID, this.gaf.sinkDistance, idMessage, this.gaf.gridID);
				this.node.broadcast(msg);
				this.gaf.battery.gastaEnergiaEnvio();
				this.gaf.state = States.discovery;
				this.gaf.startTaTimer = false;	
				//System.out.println("Time: " + Global.currentTime);
			}			
		}		
	}

}
