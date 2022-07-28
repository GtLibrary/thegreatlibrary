using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

    public class ISO_PlayerController : MonoBehaviour
    {
        #region VARIABLES
        [SerializeField] private Rigidbody _rb;
        private ISO_AnimationHandler AnimationHandler;
        [SerializeField] private float _speed = 5;
        [SerializeField] private float _turnSpeed = 360;
        private Vector3 _input;
        #endregion

        #region UNITY METHODS

        private void Awake()
        {
            AnimationHandler = GetComponent<ISO_AnimationHandler>();
        }

        private void Update() {
            GatherInput();
            Look();
        }

        private void FixedUpdate() {
            Move();
        }
        #endregion

        #region METHODS
        private void GatherInput() {
            _input = new Vector3(Input.GetAxisRaw("Horizontal"), 0, Input.GetAxisRaw("Vertical"));
        }

        private void AnimateRun()
        {
            if (_input == Vector3.zero)
            {
                AnimationHandler.SetIsMoving(false);
                return;
            }
            AnimationHandler.SetIsMoving(true);
        }

        private void Look() {
            if (_input == Vector3.zero) return;

            var rot = Quaternion.LookRotation(_input.ToIso(), Vector3.up);
            transform.rotation = Quaternion.RotateTowards(transform.rotation, rot, _turnSpeed * Time.deltaTime);
        }

        private void Move() {
            _rb.MovePosition(transform.position + transform.forward * _input.normalized.magnitude * _speed * Time.deltaTime);
            AnimateRun();

        }
        #endregion
    }
    
public static class Helpers 
{
    private static Matrix4x4 _isoMatrix = Matrix4x4.Rotate(Quaternion.Euler(0, 45, 0));
    public static Vector3 ToIso(this Vector3 input) => _isoMatrix.MultiplyPoint3x4(input);
}