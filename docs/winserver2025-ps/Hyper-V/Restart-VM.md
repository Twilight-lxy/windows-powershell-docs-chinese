---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/restart-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restart-VM
---

# 重启虚拟机

## 摘要
重启一台虚拟机。

## 语法

### 名称（默认值）
```
Restart-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-Force] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### NameWait
```
Restart-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-Force] [-AsJob] [-Passthru] [-Wait] [-For <WaitVMTypes>] [-Delay <UInt16>]
 [-Timeout <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Restart-VM [-VM] <VirtualMachine[]> [-Force] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObjectWait
```
Restart-VM [-VM] <VirtualMachine[]> [-Force] [-AsJob] [-Passthru] [-Wait] [-For <WaitVMTypes>]
 [-Delay <UInt16>] [-Timeout <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Restart-VM` cmdlet 用于重启虚拟机。运行此 cmdlet 会触发一次“强制”重启，即类似关闭计算机后再重新启动的操作。这种操作可能会导致虚拟机中的数据丢失。

## 示例

### 示例 1
```
PS C:\> Restart-VM Win7
Confirm
Are you sure you want to restart virtual machine "win7"?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
```

对虚拟机Win7执行强制重启操作。这相当于先切断虚拟机的电源，然后再重新启动它。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: Name, NameWait
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于重启虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值是本地计算机。可以通过使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name, NameWait
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name, NameWait
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Delay


```yaml
Type: UInt16
Parameter Sets: NameWait, VMObjectWait
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -For


```yaml
Type: WaitVMTypes
Parameter Sets: NameWait, VMObjectWait
Aliases:
Accepted values: Heartbeat, IPAddress

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
指定在重启虚拟机之前不会显示任何确认提示。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要重启的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: Name, NameWait
Aliases: VMName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Passthru
指定一个对象需要被传递给代表要重启的虚拟机的管道系统。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Timeout
指定等待的时间长度（以秒为单位）。当超时时间到期后，**Restart-VM** 命令会返回到命令提示符界面，即使虚拟机并未重新启动。

此参数仅与 `-Wait` 参数一起使用时才有效。`-Timeout` 参数会覆盖 `-Wait` 参数所设置的无限等待时间设置。

```yaml
Type: Int32
Parameter Sets: NameWait, VMObjectWait
Aliases: TimeoutSec

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定需要重新启动的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject, VMObjectWait
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Wait
`Restart-VM` 会抑制 PowerShell 提示符的显示，并在虚拟机重新启动之前阻塞整个命令执行流程。你可以在脚本中使用这个参数来重启虚拟机，然后在重启完成后继续执行后续操作。

`-Wait` 参数会无限期地等待虚拟机重新启动。你可以使用 `.-Timeout` 参数来调整等待时间，同时使用 `.-For` 和 `.-Delay` 参数来指定在虚拟机重启后需要等待哪些特定服务变为可用状态。

```yaml
Type: SwitchParameter
Parameter Sets: NameWait, VMObjectWait
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出。

### Microsoft.HyperV.Powershell.VirtualMachine

当你使用 **PassThru** 参数时，此 cmdlet 会返回一个 **Microsoft.HyperV.Powershell VirtualMachine** 对象。

## 备注

## 相关链接
