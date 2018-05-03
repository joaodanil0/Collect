package projects.Collect.nodes.timers;

import projects.Collect.nodes.nodeImplementations.GAF;
import projects.Collect.nodes.nodeImplementations.GAF.States;
import sinalgo.nodes.timers.Timer;

public class TsTimer extends Timer{
	
	/**
	 * The instance of the node that call the timer
	 */
	public GAF gaf;
	
	public TsTimer(GAF gaf) {
		
		this.gaf = gaf;
	}

	@Override
	public void fire() {
		
		this.gaf.state = States.discovery;
		this.gaf.startTsTimer = false;
		this.gaf.startTdTimer = false;
		this.gaf.startTaTimer = false;
		
		
		
		
	}

}
