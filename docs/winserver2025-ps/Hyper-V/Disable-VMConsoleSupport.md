---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/disable-vmconsolesupport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-VMConsoleSupport
---

# 禁用虚拟机控制台支持

## 摘要
禁用第二代虚拟机上的键盘、视频设备和鼠标功能。

## 语法

### VMName（默认值）
```
Disable-VMConsoleSupport [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Disable-VMConsoleSupport [-VM] <VirtualMachine[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-VMConsoleSupport` cmdlet 会禁用虚拟机的键盘、视频和鼠标功能。

## 示例

### 示例 1：禁用键盘、视频和鼠标支持
```
PS C:\> $VM = Get-VM -ComputerName "Server01"
PS C:\> Disable-VMConsoleSupport -VM $VM
```

第一个命令使用了 **Get-VM** cmdlet 来获取名为 Server01 的主机上的虚拟机。该命令将结果存储在 **$VM** 变量中。

第二个命令会禁用虚拟机（位于 `$VM` 目录下的那些虚拟机）对键盘、视频和鼠标的支持。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名进行识别。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确指定本地计算机。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此cmdlet会返回它所修改的`Microsoft.HyperV.VirtualMachine`对象。

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

### -VM
指定一个虚拟机数组，在这些虚拟机上，此 cmdlet 将禁用对键盘、视频和鼠标设备的支持。要获取一个 **VirtualMachine** 对象，请使用 **Get-VM** cmdlet。

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

### -VMName
指定一个虚拟机名称数组，该cmdlet将在此数组中的虚拟机上禁用对键盘、视频和鼠标的支持。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.Powershell.VirtualMachine
如果你指定了 **Passthru** 参数，此 cmdlet 会返回一个 **VirtualMachine** 对象。

## 备注

## 相关链接

[Enable-VMConsoleSupport](./Enable-VMConsoleSupport.md)

[Get-VM](./Get-VM.md)

