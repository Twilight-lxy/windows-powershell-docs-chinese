---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmdvddrive?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMDvdDrive
---

# Get-VMDvdDrive

## 摘要
获取连接到虚拟机或快照的DVD驱动器信息。

## 语法

### VMName（默认值）
```
Get-VMDvdDrive [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-ControllerLocation <Int32>] [-ControllerNumber <Int32>] [<CommonParameters>]
```

### VMObject
```
Get-VMDvdDrive [-VM] <VirtualMachine[]> [-ControllerLocation <Int32>] [-ControllerNumber <Int32>]
 [<CommonParameters>]
```

### VMSnapshot
```
Get-VMDvdDrive [-ControllerLocation <Int32>] [-ControllerNumber <Int32>] [-VMSnapshot] <VMSnapshot>
 [<CommonParameters>]
```

### VMDriveController
```
Get-VMDvdDrive [-ControllerLocation <Int32>] [-VMDriveController] <VMDriveController[]> [<CommonParameters>]
```

## 描述
`Get-VMDvdDrive` cmdlet 用于获取连接到虚拟机或快照上的 DVD 驱动器。与 `Get-VMHardDiskDrive` cmdlet 不同，该 cmdlet 没有 `ControllerType` 参数，因为虚拟 DVD 驱动器只能连接到 IDE 控制器上。

## 示例

### 示例 1
```
PS C:\> Get-VMDvdDrive -VMName Test
```

从虚拟机Test中获取虚拟DVD驱动器。

### 示例 2
```
PS C:\> Get-VM -Name Test | Get-VMDvdDrive -ControllerNumber 1
```

从虚拟机Test的IDE控制器1中获取虚拟DVD驱动器。

### 示例 3
```
PS C:\> Get-VMIdeController -VMName TestVM -ControllerNumber 1 -ComputerName Development | Get-VMDvdDrive
```

从位于 Development 服务器上的虚拟机 TestVM 的 IDE 控制器 1 中获取虚拟 DVD 驱动器。

### 示例 4
```
PS C:\> Get-VMSnapshot -VMName TestVM -Name 'Before applying updates' | Get-VMDvdDrive
```

在应用虚拟机TestVM的更新之前，从快照中获取虚拟DVD驱动器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于获取 DVD 驱动器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名进行指定。默认值是本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerLocation
指定控制器上用于获取DVD驱动器的位置编号。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定用于获取DVD驱动器的控制器的编号。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject, VMSnapshot
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定用于获取 DVD 驱动器的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMDriveController
指定用于检索DVD驱动器的控制器。

```yaml
Type: VMDriveController[]
Parameter Sets: VMDriveController
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定用于获取DVD驱动器的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSnapshot
指定要从哪个虚拟机快照中获取DVD驱动器信息。

```yaml
Type: VMSnapshot
Parameter Sets: VMSnapshot
Aliases: VMCheckpoint

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShell.VMDriveController[]

### Microsoft.HyperV.PowerShell.VMSnapshot

### Microsoft.HyperV.PowerShell.VirtualMachine[]

## 输出

### Microsoft.HyperV.PowerShell.DvdDrive

## 备注

## 相关链接

