---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmkeyprotector?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMKeyProtector
---

# Set-VMKeyProtector

## 摘要
为虚拟机配置一个密钥保护器。

## 语法

### VMName（默认值）
```
Set-VMKeyProtector [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-Passthru] [-KeyProtector <Byte[]>] [-NewLocalKeyProtector]
 [-RestoreLastKnownGoodKeyProtector] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Set-VMKeyProtector [-VM] <VirtualMachine[]> [-Passthru] [-KeyProtector <Byte[]>] [-NewLocalKeyProtector]
 [-RestoreLastKnownGoodKeyProtector] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMKeyProtector` cmdlet 用于为虚拟机配置密钥保护器。

## 示例

#### 示例 1：为虚拟机设置密钥保护器
```
PS C:\> Set-VMKeyProtector -VM $VM1 -KeyProtector $kp.RawData
```

此命令指定存储在 $VM1 变量中的虚拟机应使用位于 $kp 中的密钥保护器。

### 示例 2：通过使用虚拟机的名称来为其设置密钥保护器
```
PS C:\> Set-VMKeyProtector -VMName "VM10" -NewLocalKeyProtector
```

此命令指定名为VM10的虚拟机应使用一个新的本地密钥保护器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个用于运行该cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全合格的域名进行指定。默认值为本地计算机。可以通过使用“localhost”或点（.“”）来明确指出是本地计算机。

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
指定一个具有执行此操作权限的用户账户。默认值是当前用户。

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

### -KeyProtector
指定用于虚拟机的密钥保护器。

```yaml
Type: Byte[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewLocalKeyProtector
指定此cmdlet会生成一个新的本地密钥保护器。

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

### -Passthru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -RestoreLastKnownGoodKeyProtector
表示此cmdlet会恢复上一个已知有效的密钥保护器设置。

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
指定一个或多个虚拟机，以便为其设置密钥保护器。

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
指定一个或多个虚拟机的名称，以便为这些虚拟机设置密钥保护器。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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

### Microsoft.HyperV POWERShel.VirtualMachine

## 备注

## 相关链接

[Get-VMKeyProtector](./Get-VMKeyProtector.md)

