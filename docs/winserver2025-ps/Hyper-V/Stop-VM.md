---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/stop-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-VM
---

# 停止虚拟机

## 摘要
关闭、终止或保存虚拟机。

## 语法

### 名称（默认值）
```
Stop-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-Save] [-TurnOff] [-Force] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Stop-VM [-VM] <VirtualMachine[]> [-Save] [-TurnOff] [-Force] [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Stop-VM** cmdlet 用于关闭、断开连接或保存虚拟机。

## 示例

### 示例 1
```
PS C:\> Stop-VM -Name TestVM
```

通过客户机操作系统关闭虚拟机TestVM。

### 示例 2
```
PS C:\> Stop-VM -Name VM1 -Force
```

通过客户机操作系统关闭虚拟机TestVM，无论其中是否有未保存的应用程序数据。Hyper-V会给客户机五分钟的时间来保存数据，之后强制关闭该虚拟机。这种关闭操作可能会导致未保存的数据丢失。

### 示例 3
```
PS C:\> Stop-VM -Name TestVM -TurnOff
```

关闭虚拟机 TestVM。此操作相当于切断该虚拟机的电源供应，可能会导致未保存的数据丢失。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个用于关闭虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定的域名进行选择。默认值为本地计算机。可以使用 `localhost` 或`.` 明确表示本地计算机。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -Force
指定必须强制关闭虚拟机。如果该虚拟机上运行有未保存数据的应用程序，系统会给予该应用程序五分钟的时间来保存数据并完成关闭操作；如果虚拟机处于锁定状态，则会立即将其关闭。

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

### -Name
指定要关闭的虚拟机的名称。

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
指定要将一个 **Microsoft.HyperV.PowerShellvirtualMachine** 对象传递给管道，该对象代表需要关闭的虚拟机。

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

### -Save
指定要保存该虚拟机。

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

### -TurnOff
指定要关闭该虚拟机。

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

### -VM
指定要关闭的虚拟机。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### Microsoft.HyperV POWERShell.VirtualMachine
如果指定了 `-PassThru` 参数。

## 备注

## 相关链接

