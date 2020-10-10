import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Slide from '@material-ui/core/Slide';

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});

export default function AlertDialogSlide(props) {

    const { position, matching_skills, lacking_skills } = props.result;

    const [open, setOpen] = React.useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const capitalize = string => {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    const matchingSkills = matching_skills.map((skill, i) => {
        return <li style={{ marginBottom: '10px' }} key={i}>{capitalize(skill)}</li>
    })

    const lackingSkills = lacking_skills.map((skill, i) => {
        return <li style={{ marginBottom: '10px' }} key={i}>{capitalize(skill)}</li>
    })

    return (
        <div>
            {/* <Button variant="outlined" color="primary" onClick={handleClickOpen}> */}
            <p style={{ cursor: 'pointer' }} onClick={handleClickOpen}>{position}</p>
            {/* </Button> */}
            <Dialog
                open={open}
                TransitionComponent={Transition}
                keepMounted
                onClose={handleClose}
                aria-labelledby="alert-dialog-slide-title"
                aria-describedby="alert-dialog-slide-description"
            >
                <DialogTitle id="alert-dialog-slide-title">{"Overview"}</DialogTitle>
                <DialogContent>
                    <p className='text-muted'>Matching skills:</p>
                    <ul className='dialog-ul'>
                        {matchingSkills}
                    </ul>
                    <p className='text-muted'>Other recommended skills:</p>
                    <ul className='dialog-ul'>
                        {lackingSkills}
                    </ul>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Close
          </Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}
