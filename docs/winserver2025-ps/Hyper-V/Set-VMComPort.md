---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmcomport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMComPort
---

# 设置虚拟机的COM端口

## 摘要
配置虚拟机的COM端口。

## 语法

### VMName（默认值）
```
Set-VMComPort [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> -Number <Int32> [[-Path] <String>] [-DebuggerMode <OnOffState>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMComPort [-VM] <VirtualMachine[]> -Number <Int32> [[-Path] <String>] [-DebuggerMode <OnOffState>]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMComPort
```
Set-VMComPort [-VMComPort] <VMComPort[]> [[-Path] <String>] [-DebuggerMode <OnOffState>] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMComPort` cmdlet 用于配置虚拟机的 COM 端口。

## 示例

### 示例 1
```
PS C:\> Set-VMComPort TestVM 2 \\.\pipe\TestPipe
```

将虚拟机TestVM上的第二个COM端口配置为连接到本地计算机上的命名管道TestPipe。

> [!注意] > 之后，您可以使用第三方应用程序或自行开发的应用程序来访问这个命名管道。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
用于指定一个或多个Hyper-V主机，在这些主机上需要配置虚拟机的COM端口。可以使用NetBIOS名称、IP地址或完全限定的域名来进行指定。默认值是本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DebuggerMode
指定供调试器使用的COM端口的状态。该参数的可接受值为：On（开启）和Off（关闭）。

```yaml
Type: OnOffState
Parameter Sets: (All)
Aliases:
Accepted values: On, Off

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Number
指定要配置的COM端口的编号（1或2）。

```yaml
Type: Int32
Parameter Sets: VMName, VMObject
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **Microsoft.HyperV.PowerShell.ComPort** 对象传递给管道，该对象代表要配置的 COM 端口。

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
指定用于配置 COM 端口的命名管道路径。本地管道的格式为 “\\.\pipe\PipeName”，远程管道的格式为 “\\RemoteServer\pipe\PipeName”。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要为其配置COM端口的虚拟机。

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

### -VMComPort
指定要配置的COM端口。

```yaml
Type: VMComPort[]
Parameter Sets: VMComPort
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要为其配置COM端口的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
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
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.ComPort
如果指定了 **-PassThru** 参数。

## 备注

## 相关链接

