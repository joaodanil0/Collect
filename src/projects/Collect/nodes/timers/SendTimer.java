package projects.Collect.nodes.timers;

import projects.Collect.nodes.messages.DataMessage;
import projects.Collect.nodes.nodeImplementations.GAF;
import projects.Collect.nodes.nodeImplementations.Sink;
import projects.Collect.nodes.nodeImplementations.GAF.States;
import sinalgo.nodes.timers.Timer;

public class SendTimer extends Timer {
	
	/**
	 * The instance of the node that call the timer
	 */
	public GAF gaf;
	
	public SendTimer(GAF gaf) {
		
		this.gaf = gaf;
	}
	public static double old;
	@Override
	public void fire() {
		
		if(this.gaf.state == States.active) {
			
			int idMessage = Integer.parseInt(this.gaf.ID + "" + this.gaf.dataPctSent++);
			
			if(this.gaf.hasEnergy()) {
				GAF.dataPctsSentByHour++;
				Sink.pcktsSentByNetwork++;
				Sink.pcktsSenthour++;
				DataMessage msg = new DataMessage(this.gaf.ID, this.gaf.sinkDistance, idMessage, this.gaf.gridID);
				this.node.broadcast(msg);
				this.gaf.battery.gastaEnergiaEnvio();
			}			
		}
	}

}
