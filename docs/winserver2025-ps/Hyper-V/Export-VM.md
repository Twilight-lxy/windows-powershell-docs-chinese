---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/export-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-VM
---

# 导出虚拟机

## 摘要
将虚拟机导出到磁盘文件中。

## 语法

### 名称（默认值）
```
Export-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-Path] <String> [-AsJob] [-Passthru] [-CaptureLiveState <CaptureLiveState>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject
```
Export-VM [-VM] <VirtualMachine[]> [-Path] <String> [-AsJob] [-Passthru] [-CaptureLiveState <CaptureLiveState>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Export-VM** cmdlet 将虚拟机导出到磁盘上。该 cmdlet 会在指定位置创建一个文件夹，其中包含三个子文件夹：Snapshots（快照）、Virtual Hard Disks（虚拟硬盘）和 Virtual Machines（虚拟机）。每个子文件夹都存放着相应的文件。Snapshots 文件夹中存储着虚拟机的快照；Virtual Hard Disks 文件夹中包含该虚拟机的虚拟硬盘数据；而 Virtual Machines 文件夹则保存着该虚拟机的配置信息（以 XML 格式呈现）。

## 示例

### 示例 1
```
PS C:\> Export-VM -Name Test -Path D:\
```

将虚拟机“Test”导出到D盘的根目录中。

### 示例 2
```
PS C:\> Get-VM | Export-VM -Path D:\
```

将所有虚拟机导出到D盘的根目录下。每个虚拟机都会被导出到自己的文件夹中。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CaptureLiveState
指定 Hyper-V 如何捕获正在运行的虚拟机的内存状态。该参数的可接受值包括：

- CaptureSavedState.
Include memory state.
- CaptureDataConsistentState.
Use Production Checkpoint technology.
- CaptureCrashConsistentState.
Do nothing to handle virtual machine state.

```yaml
Type: CaptureLiveState
Parameter Sets: (All)
Aliases:
Accepted values: CaptureCrashConsistentState, CaptureSavedState, CaptureDataConsistentState

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于导出虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行选择。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要导出的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: VMName

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **Microsoft.HyperV POWERShell.VirtualMachine** 对象传递给管道，该对象代表要导出的虚拟机。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定用于导出虚拟机的文件夹的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要导出的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VirtualMachine
如果指定了**-PassThru**选项的话……

## 备注

## 相关链接

