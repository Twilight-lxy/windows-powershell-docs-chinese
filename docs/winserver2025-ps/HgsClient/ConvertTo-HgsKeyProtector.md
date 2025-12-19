---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_HgsKeyProtector_v1.0.cdxml-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/convertto-hgskeyprotector?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: ConvertTo-HgsKeyProtector
---

# 将文件转换为 HGS Key Protector 格式

## 摘要

将一个密钥保护器转换为Host Guardian Service类型的密钥保护器。

## 语法

```
ConvertTo-HgsKeyProtector [-Bytes] <Byte[]> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
[-AsJob] [<CommonParameters>]
```

## 描述

`ConvertTo-HgsKeyProtector` cmdlet 将现有的密钥保护器转换为 Host Guardian Service 密钥保护器对象。请以字节数组的形式指定该现有的密钥保护器。您可以使用此 cmdlet 从虚拟机配置文件中导入密钥保护器。

## 示例

#### 示例 1：转换密钥保护器

```powershell
$VirtualTPM = Get-VMTPM -Name "Shielded Virtual Machine 17"
$VirtualMachineKeyProtector = $VirtualTPM.KeyProtector
$KeyProtector = ConvertTo-HgsKeyProtector -Bytes $VirtualMachineKeyProtector
```

第一个命令用于获取名为“Shielded Virtual Machine 17”的虚拟机的可信平台模块（TPM）对象，并将该对象存储在 `$VirtualTPM` 变量中。

第二条命令将存储在 `$VirtualTPM` 中的对象的 **KeyProtector** 属性存储到 `$VirtualMachineKeyProtector` 变量中。

最后的命令从存储在 `$VirtualMachineKeyProtector` 中的字节数组表示中创建一个 Host Guardian Service 密钥保护器对象。该命令将新的密钥保护器存储在 `$KeyProtector` 变量中。

## 参数

### -AsJob

将 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Bytes

将现有的密钥保护器指定为一个字节数组。此cmdlet会根据该参数指定的现有密钥保护器生成一个新的密钥保护器对象。

```yaml
Type: System.Byte[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的命令行（cmdlet）操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM （Common Information Model）命令行（cmdlets）的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身的运行状态。

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_HgsKeyProtector

此 cmdlet 返回一个密钥保护器。

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[New-HgsKeyProtector](./New-HgsKeyProtector.md)
